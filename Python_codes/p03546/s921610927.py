ii = lambda : int(input())
mi = lambda : map(int,input().split())
li = lambda : list(map(int,input().split()))

h,w = mi()
c = [[float('inf') for j in range(10)]for i in range(10)]

for i in range(10):
    cc = li()
    for j in range(10):
        c[i][j] = cc[j]

# cost of i to j

for k in range(10):
    for i in range(10):
        for j in range(10):
            c[i][j] = min(c[i][j] , c[i][k] + c[k][j])

ans = 0
for i in range(h):
    w = li()
    for j in w:
        if j == -1:
            continue
        ans += c[j][1]

print(ans) 


