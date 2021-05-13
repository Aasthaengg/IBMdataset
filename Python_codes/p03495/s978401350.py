import collections
n, k = map(int, input().split())
a = list(map(int, input().split()))

d = dict(collections.Counter(a))
d = sorted(d.items(), key=lambda x:x[1])
l = len(d)

cnt = 0
for _, j in d:
    if l > k:
        l -= 1
        cnt += j

print(cnt)