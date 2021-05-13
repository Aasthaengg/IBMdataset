import sys
readline = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
#mod = 998244353
INF = 10**18
eps = 10**-7
 
x,y = map(int,readline().split())
 
if x*y > 0:
    if x > y:
        print(x-y+2)
    else:
        print(y-x)
elif x*y < 0:
    print(abs(abs(x)-abs(y))+1)
else:
    if x == 0:
        if y > 0:
            print(y)
        else:
            print(-y+1)
    else:
        if x > 0:
            print(x+1)
        else:
            print(-x)
