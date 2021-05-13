a=list(map(int,input().split()))
a.sort()
#print(a)
b1=a[2]-a[0]
b2=a[2]-a[1]

if b1%2==0 and b2%2==0:
    print(b1//2+b2//2)
elif b1%2==1 and b2%2==1:
    print(b1//2+b2//2+1)
else:
    print(b1//2+b2//2+2)
