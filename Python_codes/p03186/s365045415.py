a, b, c = map(int, input().split())
d = min(b, c)
b -= d
c -= d
e = min(c, a)
c -= e
a -= e

print(d*2 + e + b + 1 if c > 0 else d*2 + e + b + 0)
