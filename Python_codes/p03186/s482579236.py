a, b, c = map(int, input().split())
t = 0
p = 0
p = min(b, c)
b -= p
c -= p
t += p * 2
p = min(a, c)
a -= p
c -= p
t += p
t += 1 if c != 0 else 0
t += b
print(t)
