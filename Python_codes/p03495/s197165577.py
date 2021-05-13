import collections

n, k = map(int, input().split())
alis = list(map(int, input().split()))

c = collections.Counter(alis)

jun = c.most_common()[::-1]

total = len(jun)
rem = total - k


ret = 0
if rem < 0:
    print(0)
else:
    for i in range(rem):
        ret += jun[i][1]
    print(ret)
