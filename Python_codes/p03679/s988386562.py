x,a,b = map(int, input().split())
l = [x, -a, (b-a)]
if b-a <= 0: print("delicious")
elif b - a <= x and b-a > 0: print("safe")
else: print("dangerous")