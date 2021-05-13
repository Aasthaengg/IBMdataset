import collections
n = int(input())
s = [str(input()) for _ in range(n)]
m = int(input())
t = [str(input()) for _ in range(m)]
s = collections.Counter(s)
t = collections.Counter(t)

for k, j in t.items():
    if k in s:
        s[k] -= j

values, counts = zip(*s.most_common())
print(max(0,counts[0]))
