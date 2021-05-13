k, t = map(int, input().split())
a = list(map(int, input().split()))
x = max(a)
total = sum(a) - x
print(max(0, x - total - 1))