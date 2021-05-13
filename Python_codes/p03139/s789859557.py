n, a, b = map(int, input().split())
M = min(a, b)
m = max(0, a+b-n)
print(M, m)
