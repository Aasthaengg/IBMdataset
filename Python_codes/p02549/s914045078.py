N,k=map(int,input().split())
L=[0 for i in range(2)]

K=[]
for i in range(k):
    l,r=map(int,input().split())
    K.append([l,r])
mod=998244353
L[1]=1
R=[0,1]
for i in range(2,N+1):
    cnt=0
    for l,r in K:
        cnt+=R[max(0,i-l)]
        cnt-=R[max(0,i-(r+1))]
    cnt%=mod
    L.append(cnt)
    R.append(R[-1]+cnt)
print(L[-1]%mod)
#print(R)