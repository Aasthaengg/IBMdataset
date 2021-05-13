n,l = map(int, input().split())
tastes = [(i + l) for i in range(n)]
t = tastes.copy()
for j in range(n):
    t[j] = abs(t[j])
del tastes[t.index(min(t))]
print(sum(tastes))