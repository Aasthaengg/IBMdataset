a, b, k = map(int, input().split())

new_a = a - k if a >= k else 0
new_b = b - (k - a) if a < k else b
if new_b < 0:
    new_b = 0

print(new_a, end=" ")
print(new_b)