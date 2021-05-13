from math import *
d = []
l = []
for i in range(5):
    n = int(input())
    t = ceil(n/10)
    d.append(t)
    l.append(t-n/10)
print(int((sum(d) - max(l))*10))