import collections
n, k = map(int, input().split())
a = list(map(int, input().split()))
c = collections.Counter(a)
d = c.most_common()
if len(c) <= k:
    print(0)
else:
    sum = 0
    for i in range(k, len(c)):
        sum += d[i][1]
    print(sum)