from collections import Counter

N = int(input())
D = list(map(int, input().split()))
M = int(input())
T = list(map(int, input().split()))

d = Counter(D)
t = Counter(T)

f = True
for df in t.keys():
    f &= (d[df] >= t[df])

print(["NO", "YES"][f])
