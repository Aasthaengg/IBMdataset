import itertools

N, K = map(int, input().split())

td = {}

for i in range(N):
    a, b = map(int, input().split())
    td.setdefault(a, [])
    td[a].append(b)

top = []
rest = []

for k in td.keys():
    td[k].sort()
    top.append(td[k][-1])
    rest += td[k][:-1]

top.sort()
rest.sort()

cumtop = list(itertools.accumulate(reversed(top)))
cumrest = list(itertools.accumulate(reversed(rest)))

ret = 0

for i in range(min(len(top), K)):
    tmp = (i+1)*(i+1)
    tmp += cumtop[i]
    if i == K-1:
        pass
    else:
        if (K-i-2) < 0 or (K-i-2) > len(cumrest)-1:
            continue
        tmp += cumrest[(K-i-2)]
    ret = max(tmp, ret)

print(ret)

