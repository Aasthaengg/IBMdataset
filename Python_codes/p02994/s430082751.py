n, l = map(int, input().split())
taste = (l - 1) * (n - 1)
if n + l - 1 < 0:
    taste += (1 + n - 1) * (n - 1) // 2
elif l > 0:
    taste += (2 + n) * (n - 1) // 2
else:
    taste += (1 + n) * n // 2
    taste -= -l + 1
print(taste)