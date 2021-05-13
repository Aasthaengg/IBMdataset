
w,a,b = map(int,input().split())

if a <= b <= a+w:
    print(0)
elif a+w <= b:
    print(abs(b - (a+w)))
else:
    print(abs(a - (b+w)))
