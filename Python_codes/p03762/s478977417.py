n,m=map(int,input().split())
xxx=list(map(int,input().split()))
yyy=list(map(int,input().split()))
mod=10**9+7

x=[]
y=[]

for i in range(len(xxx)-1):
    x.append(xxx[i+1]-xxx[i])

for i in range(len(yyy)-1):
    y.append(yyy[i+1]-yyy[i])

cnt=0
cnt2=0


for i in range(1,len(x)+1):
    cnt+=x[i-1]*(i)*(len(x)-i+1)
    cnt%=mod

for i in range(1,len(y)+1):
    cnt2+=y[i-1]*(i)*(len(y)-i+1)
    cnt2%=mod

print((cnt*cnt2)%mod)