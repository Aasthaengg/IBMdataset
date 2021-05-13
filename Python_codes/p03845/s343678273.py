from copy import deepcopy

N = int(input())
T = list(map(int, input().split()))
M = int(input())
P, X = [], []
for _ in range(M):
    p, x = map(int, input().split())
    P.append(p)
    X.append(x)

for i in range(M):
    ans = deepcopy(T)
    ans[P[i] - 1] = X[i]
    print(sum(ans))
