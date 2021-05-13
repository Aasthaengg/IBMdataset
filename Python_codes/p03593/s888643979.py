import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


h,w = list(map(int, input().split()))
a = []
for i in range(h):
    a.extend(list(input()))
    
from collections import Counter
c = Counter(a)
# print(c)
must = {1:0, 2:0, 4:0}
must[4] += (h//2) * (w//2)
if h%2==1:
    must[2] += (w//2)
if w%2==1:
    must[2] += (h//2)
if w%2==1 and h%2==1:
    must[1] += 1
    
for base in (4,2,1):
    val = 0
    for k,v in c.items():
        if val + v//base >= must[base]:
            c[k] -= (must[base] - val) * base
            val += (must[base] - val)
#             print(c, val, v, base)
            break
        val += v//base
        c[k] -= (v//base)*base
    if val<must[base]:
        ans = "No"
        break
else:
    ans = "Yes"
print(ans)