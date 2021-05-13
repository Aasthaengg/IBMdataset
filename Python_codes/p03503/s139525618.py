n = int(input())
l = [list(map(int,input().split())) for _ in range(n)]
p = [list(map(int,input().split())) for _ in range(n)]

maxi = -10**10

for i in range(1,2**10):
    num = [0]*n
    for j in range(10):
        if ((i >> j) & 1):
            for k in range(n):
                num[k] += l[k][j]
    benefit = 0
    for m in range(n):
        benefit += p[m][num[m]]
    maxi = max(maxi,benefit)
print(maxi)