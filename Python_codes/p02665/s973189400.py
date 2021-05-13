from sys import stdin
from sys import setrecursionlimit
from itertools import accumulate
setrecursionlimit(10 ** 7)

n = int(stdin.readline().rstrip())
a = list(map(int,stdin.readline().rstrip().split()))
b = list(accumulate(a[::-1]))
b = b[::-1]
#print(b)

if n == 0:
    if a[0] == 1:
        print(1)
    else:
        print(-1)
    exit()    

if a[0] != 0:
    print(-1)
    exit()

ne = [0]*(n+1)

ne[0] = 1
point = 1

for i in range(1,n):
    point_ma = min(ne[i-1]*2,b[i+1]+a[i])
    if a[i] > point_ma:
        print(-1)
        exit()
    ne[i] = point_ma-a[i]
    point += point_ma

if ne[n-1]*2 < a[n]:
    print(-1)
    exit()

point += a[n]
ne[n] = 0

print(point)