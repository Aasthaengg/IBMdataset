a, b, k = map(int, input().split())

if a < k:
    k -= a
    a = 0
    b = 0 if b < k else b - k
else:
    a -= k
print(f'{a} {b}')