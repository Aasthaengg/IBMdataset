n=int(input())
a=list(map(int,input().split()))
mod=10**9+7

mb=format(max(a),'b')
arr=[0]*len(mb)

for i in range(n):
    b=format(a[i],'b')
    for j in range(len(b)):
        if b[-j-1]=='1':
            arr[j]+=1

ans=0

for i in range(len(mb)):
    ans+=(arr[i]*(n-arr[i])*(2**i))%mod
print(ans%mod)