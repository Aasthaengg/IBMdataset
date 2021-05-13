W, a, b = map(int, input().split())

if a < b and a+W < b :
    print(b-a-W)
elif a < b and a+W >= b :
    print(0)
elif b < a and b+W < a :
    print(a-b-W)
else :
    print(0)
