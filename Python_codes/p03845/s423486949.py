N = int(input())
T = list(map(int, input().split()))
M = int(input())
P = [None] * M
X = [None] * M

for i in range(M):
    P[i], X[i] = map(int, input().split())

for i in range(M):
    S = T.copy()
    S[P[i] - 1] = X[i]
    print(sum(S))
