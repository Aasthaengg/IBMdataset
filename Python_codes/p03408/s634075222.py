import collections
n = int(input())
s = [input() for _ in range(n)]
m = int(input())
t = [input() for _ in range(m)]
S = collections.Counter(s)
T = collections.Counter(t)
c = 0
for i, j in S.items():
    c = max(j-T[i], c)
print(c)