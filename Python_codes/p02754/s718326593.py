n, a, b = map(int, input().split())

n, m = divmod(n, a+b)
print(n*a + min(a, m))