n,T=map(int,input().split())
t=list(map(int,input().split()))
ans=0
num1=0
num2=0
for i in range(n):
    if num2>t[i]:
        num2=t[i]+T
    else:
        ans+=num2-num1
        num1=t[i]
        num2=t[i]+T
ans+=num2-num1
print(ans)
