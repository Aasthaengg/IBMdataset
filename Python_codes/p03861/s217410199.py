a, b, x = map(int, input().split())
l = (a - 1) // x
r = b // x
print(r - l)
