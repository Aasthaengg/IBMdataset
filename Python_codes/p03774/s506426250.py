from sys import exit
import math
ii = lambda : int(input())
mi = lambda : map(int,input().split())
li = lambda : list(map(int,input().split()))

n,m=mi()
a =  [list(map(int, input().split())) for i in range(n)]
c =  [list(map(int, input().split())) for i in range(m)]

INF = 100000000000
dis = INF
ans = 0
for i in range(n):
    for j in range(m):
        if abs(a[i][0]-c[j][0]) + abs(a[i][1]-c[j][1]) < dis:
            dis = abs(a[i][0]-c[j][0]) + abs(a[i][1]-c[j][1])
            ans = j+1

    print(ans)
    dis = INF
    ans = 0