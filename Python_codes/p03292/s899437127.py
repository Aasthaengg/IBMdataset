a, b, c = map(int, input().split())

l = []

s = 0
s += abs(b - a)
s += abs(c - b)
l.append(s)

s = 0
s += abs(c - a)
s += abs(b - c)
l.append(s)

s = 0
s += abs(a - b)
s += abs(c - a)
l.append(s)

s = 0
s += abs(c - b)
s += abs(a - c)
l.append(s)

s = 0
s += abs(a - c)
s += abs(b - a)
l.append(s)

s = 0
s += abs(b - c)
s += abs(a - b)
l.append(s)

print(min(l))