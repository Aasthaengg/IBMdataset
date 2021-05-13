N = int(input())
S = [("R", "G", "B").index(c) for c in input()]

sums = [[0] * (N + 1) for _ in range(3)]
for i, c in enumerate(S):
    for x in sums:
        x[i+1] = x[i]
    sums[c][i+1] += 1

ans = 0
for i in range(N - 2):
    si = S[i]
    for j in range(i + 1, N - 1):
        sj = S[j]
        if si == sj:
            continue
        sk = (set(range(3)) - {si, sj}).pop()
        count = sums[sk][N] - sums[sk][j+1]
        if j - i <= N - (j + 1):
            count -= (sums[sk][j+1+j-i] - sums[sk][j+1+j-i-1])
        ans += count
print(ans)