n,k=map(int,input().split())
X=list(map(int,input().split()))
for i in range(n):
    if X[i]>=0:
        break
else:
    i=n

if i==0:
    M=[]
else:
    M=X[i-1::-1]
if i==n:
    P=[]
else:
    P=X[i:]
    
ans=10**10
for j in range(k+1):
    if len(M)<j or len(P)<k-j:
        continue
    if j==0:
        ans=min(P[k-1],ans)
    elif j==k:
        ans=min(-M[k-1],ans)
    else:
        l=max(-M[j-1],P[k-j-1])
        s=min(-M[j-1],P[k-j-1])
        ans=min(s*2+l,ans)
print(ans)