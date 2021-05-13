a, b = map(int, input().split())
max_value = a + b
if a - b > max_value:
    max_value = a - b
if a * b > max_value:
    max_value = a * b
print(max_value)