n = int(input())
yaku = [0]*101
from collections import Counter

def pf(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

for i in range(2,n+1):
    c = pf(i)
    for j in c:
        yaku[j] += 1
        
b = Counter(yaku)
ans = 0
aa = 0
for i in range(4,101):
    aa += b[i]
    
ans += (b[2]+b[3]) * aa * (aa-1) // 2
ans += aa * (aa-1) * (aa-2) // 2

aa = 0
for i in range(74,101):
    aa += b[i]
ans += aa

aa = 0
for i in range(24,101):
    aa += b[i]
bb = 0
for i in range(2,101):
    bb += b[i]
ans += (bb-1) * aa

aa = 0
for i in range(14,101):
    aa += b[i]
bb = 0
for i in range(4,101):
    bb += b[i]
ans += (bb-1) * aa

print(ans)