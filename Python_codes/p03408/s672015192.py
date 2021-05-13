import collections
n = int(input())
lb = [input() for _ in range(n)]
m = int(input())
la = [input() for _ in range(m)]


cntb = collections.Counter(lb)
cnta = collections.Counter(la)
t_max = 0
cntb.subtract(cnta)

m = sorted(cntb.items(), key=lambda x: x[1], reverse=True)
print(max(0, m[0][1]))
