a, b, c = map(int, input().split())
if b + c >= a:
    c = b + c - a
else:
    c = 0
print(c)
