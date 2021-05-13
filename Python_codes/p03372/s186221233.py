import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)
from itertools import accumulate
n,c=map(int,input().split())
X,V=[],[]
for _ in range(n):
    x,v=map(int, input().split())
    X.append(x)
    V.append(v)
V_ret,X_ret=V[::-1],X[::-1]
S,S_ret=list(accumulate(V)),list(accumulate(V_ret))
S[0]-=X[0]
S_ret[0]-=(c-X_ret[0])
for i in range(1,n):
    S[i]=max(S[i-1],S[i]-X[i])
    S_ret[i]=max(S_ret[i-1],S_ret[i]-(c-X_ret[i]))
ans=max(0,max(S),max(S_ret))
for i in range(n-1):
    tmp1=S[i]+S_ret[n-(i+2)]-X[i]
    tmp2=S_ret[i]+S[n-(i+2)]-(c-X_ret[i])
    ans=max(ans,tmp1,tmp2)
print(ans)