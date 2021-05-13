from bisect import bisect_left
from bisect import bisect_right



n,m=map(int, input().split())
A=list(map(int, input().split()))
A.sort()
S=[0]*(n+1)
for i in range(1,n+1):
    S[i]=S[i-1]+A[i-1]

def solve(x):
    case=0
    for i in range(n):
        case+=n-bisect_right(A,x-A[i]-1)
    return case

right=2*A[-1]+1
left=0
         
while abs(right-left)>1:
    mid=(right+left)//2
    if solve(mid)>=m:
        left=mid
    else:
        right=mid
    
Kijun=left
ans=0
for i in range(n):
    case=n-bisect_right(A,Kijun-A[i]-1)
    ans+=case*A[i]+(S[n]-S[n-case])
    
ans-=(solve(Kijun)-m)*Kijun
print(ans)