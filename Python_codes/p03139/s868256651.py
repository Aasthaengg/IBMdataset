n, a, b = map(int, input().split())
max_value = min(a, b)
if a + b - n < 0:
    min_value = 0
else:
    min_value = a + b - n
print(f'{max_value} {min_value}')