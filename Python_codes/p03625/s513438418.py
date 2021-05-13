n=int(input())
a=list(map(int,input().split()))
a.sort(reverse=True)
num1=0
num2=0
ans=1
for i in range(n):
    if a[i]==num1:
        ans*=a[i]
        num2+=1
        num1=0
    else:
        num1=a[i]
    if num2==2:
        break
if num2==2:
    print(ans)
else:
    print(0)
