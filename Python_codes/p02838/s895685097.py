n=int(input())
a=[int(x) for x in input().split()]
keta_0=[0]*70
keta_1=[0]*70
for shift in range(70):
    for i in range(n):
        if a[i]>>shift & 1:
            keta_1[shift]+=1
        else:
            keta_0[shift]+=1
ans=0

for i in range(70):
    ans+=2**i*keta_0[i]*keta_1[i]
    ans%=10**9+7

print(ans)