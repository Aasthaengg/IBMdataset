n = int(input())
slist = []
for i in range(n):
    s = input()
    slist.append(s[0])
import collections
c = collections.Counter(slist)
l = ["M","A","R","C","H"]
import itertools
citer = list(itertools.combinations(l,3))
ans = 0
for i in citer:
    ans += c[i[0]] * c[i[1]] * c[i[2]]
print(ans)