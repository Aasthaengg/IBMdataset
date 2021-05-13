from sys import stdin
def input():
    return stdin.readline().strip()

n = int(input())

def adjust(x, y):
    if x % y == 0:
        return x // y
    else:
        return x//y + 1

ta, ao = 1, 1
for _ in range(n):
    t, a = map(int, input().split())
    mul = max([adjust(ta, t), adjust(ao, a)])
    ta = mul * t
    ao = mul * a

print(ta + ao)