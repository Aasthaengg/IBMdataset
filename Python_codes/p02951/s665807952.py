
a, b, c = map(int, input().split())
res = 0
if a < b+c:
    res = b + c - a
else:
    res = 0
print(res)
