x,a,b = [int(x) for x in input().split()]

if a-b >= 0:
    print("delicious")
elif b-a > 0 and b-a <= x:
    print("safe")
else:
    print("dangerous")