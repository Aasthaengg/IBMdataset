n=int(input())
p=10**9+7
a=list(map(int,input().split()))
bit=[0]*61
for i in range(n):
    b=bin(a[i])[2:].zfill(61)
    for j in range(61):
        if b[j]=="1":
            bit[j]+=1
ans=0
for i in range(61):
    x=bit.pop()
    ans+=x*(n-x)*(2**i)%p
print(ans%p)