x, a, b = map(int, input().split())

if a >= b:
    print("delicious")
elif x + 1 > abs(a - b):
    print("safe")
else:
    print("dangerous")