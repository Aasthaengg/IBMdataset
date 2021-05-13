N=int(input())
A=list(map(int,input().split()))
c=[0]*(N+1)
c[0]=3
cnt=1
mod=10**9+7
for i in A:
    cnt=cnt*c[i]%mod
    c[i]-=1
    c[i+1]+=1
print(cnt)