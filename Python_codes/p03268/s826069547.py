n, k = map(int, input().split())
res = (n // k) ** 3
if not k & 1:
    res += (2 * n // k - n // k) ** 3
print(res)