N = int(input())
X = [int(x) for x in input().split()]

ind = [i for i in range(N)]
# XのindexをXが昇順になるように並び替える
ind = sorted(ind, key = lambda i : X[i])
ans = [0] * N
for i in range(N // 2):
    ans[ind[i]] = X[ind[N // 2]]
for i in range(N // 2, N):
    ans[ind[i]] = X[ind[N // 2 - 1]]

for i in range(N):
    print(ans[i])