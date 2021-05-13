MOD = 10**9 + 7
import sys
input = sys.stdin.readline
from functools import reduce
from itertools import starmap
n,m = map(int,input().split())
x = list(map(int,input().split()))
y = list(map(int,input().split()))

mulmod = lambda x,y : (x*y) % MOD
summod = lambda x,y : (x+y) % MOD
coefx = range(-(n-1),n+1,2)
xds = reduce(summod, starmap(mulmod, zip(x,coefx)))
coefy = range(-(m-1),m+1,2)
yds = reduce(summod, starmap(mulmod, zip(y,coefy)))

print((xds*yds) % MOD)

