a, b, c = map(int, input().strip().split(' '))
if b>=c:
    print(b+c)
elif a+b>=c:
    print(b+c)
else:
    print(a+2*b+1)