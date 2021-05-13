n, t = map(int, input().split())
ns = list(map(int, input().split()))
min_n = 10 ** 10
max_n = 0
max_l = []
for i in ns[::-1]:
    max_n = max(max_n, i)
    max_l.append(max_n)
max_l.reverse()
l = []
for i in range(n):
    l.append(ns[i]-min_n)
    min_n = min(min_n, ns[i])
print(l.count(max(l)))