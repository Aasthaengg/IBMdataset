import collections
a = list(input())
c = collections.Counter(a)
n = len(a)
ans = n*(n-1)//2 + 1
for v in c.values():
    ans -= v*(v-1)//2
print(ans)