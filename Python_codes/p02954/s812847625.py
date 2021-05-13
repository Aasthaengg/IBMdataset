LOG = 18  # log2(10**5)
S = input()
N = len(S)
to = [[0] * N for _ in range(LOG)]

for i in range(N):
    to[0][i] = i + 1 if S[i] == 'R' else i - 1

for i in range(1, LOG):
    for j in range(N):
        to[i][j] = to[i - 1][to[i - 1][j]]

ans = [0] * N
for i in range(N):
    ans[to[LOG - 1][i]] += 1

L = [str(i) for i in ans]
print(' '.join(L))
