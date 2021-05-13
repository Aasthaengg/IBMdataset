x, y, z = map(int, input().split())
if y >= z:
    print("delicious")
elif x - z + y >= 0:
    print("safe")
else:
    print("dangerous")
