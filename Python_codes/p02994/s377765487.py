n,l = map(int, input().split())
if l > 0:
    x = 1
elif n + l < 1:
    x = n
else:
    x = 1 - l
print(int(1 - l - x + n * (2 * l + n - 1) / 2))