n, a, b = map(int, input().split())
MAX = min(a, b)
MIN = max(0, a+b-n)
print(MAX, MIN)