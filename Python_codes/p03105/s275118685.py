a, b, c = map(int,input().split())

if b - (a * c) >= 0:
    print(c)

elif b - (a * c) < 0:
    print(b // a)

elif a > b :
    print(0)
