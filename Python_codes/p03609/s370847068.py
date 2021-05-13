import sys
X,t = map(int,input().split())
if X < 0 or t < 0 or X > 10 ** 9 or t > 10 ** 9:
    sys.exit()

if (X - t) <= 0:
    print(0)
else:
    print(int(X - t))