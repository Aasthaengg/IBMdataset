import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

x,y = map(int,readline().split())
if abs(x) == abs(y):
    if x == y:
        print(0)
    else:
        print(1)
    exit()
need = min(abs(x-y),abs(x+y))
if abs(x) <= abs(y):
    grad = "+"
else:
    grad = "-"

if grad == "+" and x < 0:
    need += 1
if grad == "-" and x > 0:
    need += 1

if grad == "+" and y < 0:
    need += 1
if grad == "-" and y > 0:
    need += 1

print(need)