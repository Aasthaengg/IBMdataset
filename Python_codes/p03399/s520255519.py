a = int(input())
b = int(input())
c = int(input())
d = int(input())
n = 0
if a <= b:
    n += a
else:
    n += b
if c <= d:
    n += c
else:
    n += d
print(n)