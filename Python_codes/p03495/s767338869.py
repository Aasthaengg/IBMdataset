import collections
n,k = map(int, input().split())
a = list(map(int, input().split()))
l = collections.Counter(a)
p = list(l.values())
p.sort()
ans = 0
for i in range(len(p)-k):
    ans += p[i]
print(ans)