n=int(input())
a=list(map(int,input().split()))
a.sort()
num1=a[0]
num2=1
ans=0
for i in range(n-1):
    if num1==a[i+1]:
        num2+=1
    else:
        if num2<num1:
            ans+=num2
        else:
            ans+=num2-num1
        num1=a[i+1]
        num2=1
if num2>1:
    if num2<num1:
        ans+=num2
    else:
        ans+=num2-num1
else:
    if num1>1:
        ans+=1
print(ans)
