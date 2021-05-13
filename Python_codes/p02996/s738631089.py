import sys
sys.setrecursionlimit(10**6)

n = int(input())

readline = sys.stdin.readline

d = {}

for _ in range(n):
    a,b = [int(i) for i in readline().split()]
    d[b] = d.get(b, 0) + a

d_sorted = sorted(d.items(), key=lambda x:x[0])

s = 0
for t, w in d_sorted:
    s += w
    if s > t:
        print('No')
        break
else:
    print('Yes')