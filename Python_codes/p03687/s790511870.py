import collections

s = list(input())
c = collections.Counter(s)

lm = list()
for i in list(c.keys()):
    l = [-1]
    for j in range(len(s)):
        if s[j] == i:
            l.append(j)
    l.append(len(s))
    lm.append(max([l[k+1]-l[k]-1 for k in range(len(l)-1)]))

print(min(lm))