import sys
import math
import itertools as it
def I():return int(sys.stdin.readline().replace("\n",""))
def I2():return map(int,sys.stdin.readline().replace("\n","").split())
def S():return str(sys.stdin.readline().replace("\n",""))
def L():return list(sys.stdin.readline().replace("\n",""))
def Intl():return [int(k) for k in sys.stdin.readline().replace("\n","").split()]
def Lx(k):return list(map(lambda x:int(x)*-k,sys.stdin.readline().replace("\n","").split()))

n = I()
h = Intl()
h = h[::-1]
cnt = 0
ans = 0
for i in range(n-1):
    if h[i] <= h[i+1]:
        cnt += 1
    else:
        cnt = 0
    ans = max(cnt,ans)
print(ans)