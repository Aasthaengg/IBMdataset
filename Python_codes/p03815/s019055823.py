import sys
def I(): return int(sys.stdin.readline().rstrip())

x = I()

q = (x-1)//11
r = (x-1) % 11
print(2*q+1 if r <= 5 else 2*q+2)
