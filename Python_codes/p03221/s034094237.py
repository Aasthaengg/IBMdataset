from collections import defaultdict

N, M = map(int, input().split())
IPY = []
for i in range(1, M + 1):
    p, y = map(int, input().split())
    IPY.append((i, p, y))
IPY.sort(key=lambda ipy: ipy[2])

ids = {}
nums = defaultdict(int)
for i, p, y in IPY:
    nums[p] += 1
    ids[i] = '{:06d}{:06d}'.format(p, nums[p])
for i in range(1, M + 1):
    print(ids[i])