k, t = map(int, input().split())
a = list(map(int, input().split()))

maxA = max(a)
# print(a)
t = a.index(maxA)
# 最大を置いて，間に挟んでいく
# 間に挟める個数はk - a[t]個ある
# a[t] - 1個はdefault
ans = max(a[t] - 1 - (k - a[t]), 0)
print(ans)