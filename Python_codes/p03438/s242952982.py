n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c,d=0,0
for i in range(n):
    if a[i]>b[i]:
        c+=a[i]-b[i]
    else:
        d+=(b[i]-a[i])//2
if d>=c:
    print("Yes")
else:
    print("No")