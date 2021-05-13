a,b = map(int, input().split())

if a-b >= 2:
    print(a+(a-1))
elif b-a >= 2:
    print(b+(b-1))
else:
    print(a+b)