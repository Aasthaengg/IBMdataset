x, a, b = map(int, input().split())

a *= -1

a += b

if a <= 0:
    print("delicious")
elif a <= x:
    print("safe")
else:
    print("dangerous")