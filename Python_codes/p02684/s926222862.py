n, k = map(int, input().split())
A = list(map(int, input().split()))
A = [a-1 for a in A]

L = 65
D = [[0]*n for _ in range(L+1)]

for i, a in enumerate(A):
    D[0][i] = a

for i in range(L):
    for j in range(n):
        D[i+1][j] = D[i][D[i][j]]

ans = 0
for i in range(L):
    if k & (1 << i):
        ans = D[i][ans]
print(ans+1)
