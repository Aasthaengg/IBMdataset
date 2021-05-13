
N, K = map(int, input().split())
S = input()

q = [(S[0], 0)]
cur = S[0]
for i in range(1, N):
    if S[i] != cur:
        q.append((S[i], i))
        cur = S[i]

lim = len(q)
ans = []
for i in range(lim):
    if q[i][0] == "0":
        j = i + 2 * K
    else:
        j = i + 2 * K + 1

    if j < lim:
        ans.append(q[j][1] - q[i][1])
    else:
        ans.append(N - q[i][1])

print(max(ans))
