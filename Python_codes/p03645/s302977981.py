n, m = map(int, input().split())
AB = []
import collections
d = collections.defaultdict(list)
for i in range(m):
    a,b = map(int, input().split())
    #AB.append(ab)
    d[a].append(b)
    d[b].append(a)
for k in d.keys():
    if 1 in d[k] and n in d[k]:
        print('POSSIBLE')
        exit()
print('IMPOSSIBLE')