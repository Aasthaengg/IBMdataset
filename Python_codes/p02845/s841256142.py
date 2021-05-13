n = int(input())
li = list(map(int,input().split()))

xyz = [[0,0,0]for _ in range(n)]
xyz[0] = [0,0,0]

mod = 10**9+7

for i in range(n-1):
    if li[i] not in xyz[i]:
        print(0)
        exit()
    ix = xyz[i].index(li[i])
    for j in range(3):
        if j == ix:
            xyz[i+1][j] = xyz[i][j] + 1
        else:
            xyz[i+1][j] = xyz[i][j]

point = 3

for i in range(1,n):
    point *= xyz[i].count(li[i])
    point %= mod
print(point)