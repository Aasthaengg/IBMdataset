n = int(input())
from bisect import bisect 
ab = [list(map(int,input().split())) for i in range(n)]

ab.sort(key = lambda x: x[1])
ok = True
last = 0
for a,b in ab:
    if b-a>=last:
        last += a
    else:
        ok = not ok
        break
print('Yes' if ok else 'No')