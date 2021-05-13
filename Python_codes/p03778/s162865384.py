w,a,b=[int(i) for i in input().split()]

if a+w<b:
    print(abs(b-a-w))
elif b+w<a:
    print(abs(a-b-w))
else:
    print(0)