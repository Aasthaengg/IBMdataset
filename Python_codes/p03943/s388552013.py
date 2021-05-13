a=list(map(int,input().split()))
a.sort()
b=a[0]+a[1]
c=a[2]
if b==c:
    print("Yes")
else:
    print("No")
