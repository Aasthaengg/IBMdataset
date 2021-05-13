h,n=map(int,input().split())
a=list(map(int,input().split()))

a.sort(reverse=True)

ans=0
power=0
for i in range(n):
    power+=a[i]
    if power>=h:
        ans=1
        break
if ans==1:
    print("Yes")
else:
    print("No")
