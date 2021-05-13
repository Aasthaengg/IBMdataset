import collections

n = int(input())
s = list(input() for i in range(n))
s = sorted(s)
c = collections.Counter(s)
p = max(c.values())
s = sorted(list(set(s)))

for i in range(len(s)):
    if c[s[i]] == p:
        print(s[i])