def MAP(): return map(int, input().split())
a, b = MAP()
n = b - a
print(n * (n + 1) // 2 - b)