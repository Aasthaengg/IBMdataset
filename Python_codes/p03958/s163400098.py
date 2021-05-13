k, t = map(int, input().split())
a = list(map(int, input().split()))
ma = max(a)
s = sum(a) - ma
print(max(0, ma - s - 1))