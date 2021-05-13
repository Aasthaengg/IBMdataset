from collections import defaultdict

n, m = map(int, input().split())
py = []
lst = [[] for _ in range(n)]
for _ in range(m):
    tmp = list(map(int, input().split()))
    py.append((tmp[0], tmp[1]))
    lst[tmp[0] - 1].append(tmp[1])
dic = {}
for i, l in enumerate(lst):
    l.sort()
    for j, num in enumerate(l):
        dic[(i + 1, num)] = "{:06}".format(i + 1) + "{:06}".format(j + 1)
for l in py:
    print(dic[l])
