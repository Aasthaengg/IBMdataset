n,m=map(int,input().split())
num1=0
ans=1
num=[0,1]
for i in range(n):
    num.append(num[-1]+num[-2])
for i in range(m):
    a=int(input())
    if num1==a:
        ans=0
        break
    else:
        ans*=num[a-num1]
        ans%=10**9+7
        num1=a+1
ans*=num[n-num1+1]
ans%=10**9+7
print(ans)
