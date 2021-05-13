import sys
from itertools import accumulate
input = sys.stdin.readline

n,k=map(int,input().split())
L=list(map(int,input().split()))
M=[(1+i)/2 for i in L]
N=[0]+list(accumulate(M))
ans = 0
for i in range(k,n+1):
    val = N[i]-N[i-k]
    ans = max(val,ans)
print("%.6f"%ans)
