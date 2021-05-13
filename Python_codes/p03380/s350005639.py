n=int(input())
a=list(map(int,input().split()))
a.sort()
num1=a[-1]
num2=a[-1]/2
num3=a[-1]
ans=-1
for i in range(n-1):
    if abs(a[i]-num2)<num3:
        ans=a[i]
        num3=abs(a[i]-num2)
print(num1,ans)
