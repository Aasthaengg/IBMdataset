n, k, s = map(int, input().split())
a = [s] * k
b = [pow(10, 9) if not s == pow(10, 9) else 1] * (n - k)
print(" ".join(map(str, a + b)))