import sys
def I(): return int(sys.stdin.readline().rstrip())

x = I()

q = x//11
r = x % 11
if r == 0:
    print(2*q)
elif 1 <= r <= 6:
    print(2*q+1)
else:
    print(2*q+2)