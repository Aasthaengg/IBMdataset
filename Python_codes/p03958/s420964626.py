k, t = map(int, input().split())
a = max(map(int, input().split()))
print(max(a - 1 - (k - a), 0))
