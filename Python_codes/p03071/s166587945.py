a, b = map(int, input().split())
print(a == b and a * 2 or max(a, b) * 2 - 1)