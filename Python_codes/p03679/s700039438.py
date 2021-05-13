x,a,b = map(int, input().split())
if b-a < 1:
    print("delicious")
elif b-a < x + 1:
    print("safe")
else:
    print("dangerous")