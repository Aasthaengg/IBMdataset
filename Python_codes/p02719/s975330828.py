n, k = map(int, input().split())
x = n % k
x = min(x, k - x)
n = x
print(n)