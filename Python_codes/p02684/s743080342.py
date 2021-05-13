N, K = list(map(int, input().split()))
A = [0]+list(map(int, input().split()))
n = 1
c = 0
while n <= K:
    n *= 2
    c += 1
# print(c)
L = [[0]*(N+1) for _ in range(c)]
L[0] = A
for i in range(1, c):
    for j in range(N+1):
        L[i][j] = L[i-1][L[i-1][j]]
# print(L)

p = 1
for i in range(c):
    if (K >> i) & 1:
        p = L[i][p]
print(p)