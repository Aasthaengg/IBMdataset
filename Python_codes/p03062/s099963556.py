N=int(input())
A=list(map(int,input().split()))

mi=10**9+1
S=0
cnt=0
for i in range(N):
    if A[i]<0:
        cnt+=1
    a=abs(A[i])
    S+=a
    mi=min(mi,a)

if cnt%2==0:
    ans=S
else:
    ans=S-2*mi
print(ans)