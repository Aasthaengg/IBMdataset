k, a, b = map(int, input().split())
n = min(a - 1, k) + 1
k -= (n - 1)
if a + 2 <= b:
    n += (k // 2) * (b - a)
    n += k % 2
else:
    n += k
print(n)