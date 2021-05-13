a,b = map(int,input().split())
if a + b > a * b:
    if a + b > a - b:
        print(a + b)
    else:
        print(a - b)
elif a * b > a - b:
    if a * b > a - b:
        print(a * b)
    else:
        print(a - b)
else:
    print(a - b)