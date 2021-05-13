a, b = map(int, input().split())

if a > 0 and b > 0 or a < 0 and b < 0:
    if a > b:
        print(a-b+2)
    else:
        print(b-a)
elif abs(a) == abs(b):
    print(1)
else:
    if b == 0 and a > b:
        print(abs(abs(a)-abs(b))+1)
    elif b == 0:
        print(abs(abs(a)-abs(b)))
    elif a == 0 and b > 0:
        print(abs(abs(a)-abs(b)))
    else:
        print(abs(abs(a)-abs(b))+1)
