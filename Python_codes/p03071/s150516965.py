a, b = map(int, input().strip().split())

res = 0
if a < b:
    res = 2 * b - 1
elif a == b:
    res = 2 * a
else:
    res = 2 * a - 1

print(res)
