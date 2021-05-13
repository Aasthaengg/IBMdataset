a, b, c = map(int, input().split())

tmp = a
a = b
b = tmp

tmp = a
a = c
c = tmp

print(f"{a} {b} {c}")
