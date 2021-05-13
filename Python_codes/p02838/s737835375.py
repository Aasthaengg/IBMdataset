n=int(input())
a=list(map(int,input().split()))
num=[0]*63
for i in range(n):
    num1=a[i]
    for j in range(63):
        if num1==0:
            break
        if num1%2==1:
            num[j]+=1
        num1//=2
ans=0
for i in range(63):
    if num[i]!=0 and num[i]!=n:
        ans+=((2**i)*num[i]*(n-num[i]))%(10**9+7)
ans%=10**9+7
print(ans)
