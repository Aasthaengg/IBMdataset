from collections import Counter

n, k = map(int, input().split())
a = list(map(int, input().split()))

c = Counter(a)
c = dict(sorted(c.items(), key=lambda x:x[1], reverse=True))

ans = sum(list(c.values())[k:])
print(ans)
