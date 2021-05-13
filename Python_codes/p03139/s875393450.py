a, b, c = map(int, input().split())

t = min(b, c)

if b+c < a:
    s = 0
else:
    s = b + c - a
print(t, s)