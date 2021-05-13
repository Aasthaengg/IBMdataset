import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

n,c = map(int,readline().split())
xv = []
l1 = []
for i in range(n):
    x,v = map(int,readline().split())
    xv.append([x,v])
    l1.append(v)
l2 = l1[::]
r1 = l1[::-1]
r2 = r1[::]


for i in range(1, n) :
    l1[i] += l1[i-1]
    l2[i] += l2[i-1]
    r1[i] += r1[i-1]
    r2[i] += r2[i-1]

for i in range(n) :
    x = xv[i][0]
    l1[i] -= x
    l2[i] -= 2 * x
    r1[n-1-i] -= c - x
    r2[n-1-i] -= 2 * (c - x)
 
for i in range(1, n) :
    l1[i] = max(l1[i], l1[i-1])
    r1[i] = max(r1[i], r1[i-1])
 
res = max(l1[-1], r1[-1])
for i in range(n-1) :
    res = max(res, l2[i] + r1[n-2-i])
    res = max(res, r2[i] + l1[n-2-i])
    
print(max(res, 0))