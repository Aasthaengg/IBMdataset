import sys
def I(): return int(sys.stdin.readline().rstrip())

X = I()
q,r = X//100,X%100
if q*5 >= r:
    print(1)
else:
    print(0)
