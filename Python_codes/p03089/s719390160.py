N = int(input())
B = list(map(int, input().split()))

out = []

for i in range(N):
    cand = []
    for j in range(len(B)):
        if B[j] == j + 1:
            cand.append(j)
    if len(cand) > 0:
        candmax = max(cand)
        out.append(candmax + 1)
        del B[candmax]
    else:
        print(-1)
        exit()
print(*out[::-1])
