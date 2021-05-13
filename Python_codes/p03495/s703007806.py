import collections

n, k = map(int, input().split())
a = list(map(int, input().split()))

b = collections.Counter(a)
b = list(b.values())
b.sort()
ans = 0
for i in range(len(set(a))-k):
    ans += b[i]
print(ans)