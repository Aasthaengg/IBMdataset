x, a, b = map(int, input().split())
c = -a + b
if c <= 0:
    print("delicious")
elif c <= x:
    print("safe")
else:
    print("dangerous")