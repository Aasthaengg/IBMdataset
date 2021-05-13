l=list(input())
n=len(l)
p=10**9+7
dp1=[0]*n
dp2=[0]*n
dp1[0]=1
dp2[0]=2
for i in range(1,n):
    if l[i]=="1":
        dp1[i]=(3*dp1[i-1]+dp2[i-1])%p
        dp2[i]=(dp2[i-1]*2)%p
    else:
        dp1[i]=(3*dp1[i-1])%p
        dp2[i]=dp2[i-1]
print((dp1[n-1]+dp2[n-1])%p)
