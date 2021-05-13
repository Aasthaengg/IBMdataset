n=int(input())
a=list(map(int,input().split()))
ave=sum(a)/n
count=1000000000
ans=0
for j in range(len(a)):
    if abs(a[j]-ave)<count:
        count=abs(a[j]-ave)
        ans=j
print(ans)