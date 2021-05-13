n=int(input())
a=list(map(int,input().split()))
ave=sum(a)/n
ans=0
num=n
for i in range(n):
    if abs(a[i]-ave)<num:
        ans=i
        num=abs(a[i]-ave)
print(ans)
