n, m = map(int, input().split())
x = (1900 * m + (n - m) * 100) * pow(2, m)
print(x)