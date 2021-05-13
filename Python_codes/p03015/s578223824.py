import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
from itertools import product
def resolve():
    L=input()
    dp=[0]*2
    dp[0]=1
    for l in L:
        l=int(l)
        ndp=[0]*2
        for a,b,lt in product(range(2),repeat=3):
            if(a*b): continue
            if((not lt) and (a+b>l)): continue
            ndp[max(lt,a+b<l)]+=dp[lt]
            ndp[max(lt,a+b<l)]%=MOD
        dp=ndp
    print(sum(dp)%MOD)
resolve()