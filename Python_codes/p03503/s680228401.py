n = int(input())
F = [[int(x) for x in input().split()] for i in range(n)]
P = [[int(x) for x in input().split()] for i in range(n)]
res = -10**12
for bit in range(1, 2 ** 10):
    cc = 0
    for i in range(n):
        cc += P[i][sum([(F[i][j]==1 and (1 & (bit >> j))==True) for j in range(10)])]
    res = max(res, cc)
print(res)
