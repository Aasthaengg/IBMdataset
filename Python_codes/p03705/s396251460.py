n, a, b = map(int, input().split())
print(max(0, a + (n-1)*b - (n-1)*a - b + 1))