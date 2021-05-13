k, t = map(int, input().split())
a = map(int, input().split())

x = max(a)
y = (k - x)

r = x - y - 1
print(max(0, r))
