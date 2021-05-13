import collections

n = int(input())
s = [''] * n
for i in range(n):
    s[i] = input()

cs = collections.Counter(s)
mcs = cs.most_common()
cnt = mcs[0][1]

fcs = [i[0] for i in cs.items() if i[1] == cnt]
ans = sorted(fcs)
for s in ans:
    print(s)
