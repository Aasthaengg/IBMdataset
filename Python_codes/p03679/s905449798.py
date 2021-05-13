x, a, b = map(int, input().split())
if b <= a:
    print("delicious")
elif (b - a) <= x and b >= a:
    print("safe")
else:
    print("dangerous")