a,b,c = map(int,input().split())

if c < a+b:
    print(b+c)
elif a+b < c:
    print(b+(b+a)+1)
else:
    print(b+(b+a))