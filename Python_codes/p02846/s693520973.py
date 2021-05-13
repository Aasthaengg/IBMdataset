import sys

t1, t2 = map(int, input().split())
a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())

p1 = (b1 - a1) * t1
p2 = (b2 - a2) * t2

if p1 + p2 == 0:
    print('infinity')
    sys.exit()

if p1 + p2 < 0:
    p1 *= -1
    p2 *= -1

if p1 > 0:
    print(0)
    sys.exit()

ans = int((-1 * p1) / (p1+p2)) * 2 + 1

if (-1 * p1) % (p1+p2) == 0:
    ans -= 1

print(ans)
