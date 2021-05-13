import collections
n = int(input())
a = list(map(int, input().split()))
c = collections.Counter(a)
v = c.values()
s = 0
for i in v:
    s += (i*(i-1))//2

for i in range(n):
    d = c[a[i]]
    x = (d*(d-1))//2 if d > 1 else 0
    y = ((d-1)*(d-2))//2 if d > 2 else 0
    print(s-x+y)
