n, k = map(int, input().split())
x = n // k
res = x*x*x
if k % 2 == 0 and k//2 <= n:
    x = n - (k//2)
    x = x // k
    x += 1
    res += x*x*x
print(res)
