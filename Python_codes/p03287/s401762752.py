from itertools import accumulate
import collections
n , m = map(int,input().split())
a = list(map(int,input().split()))

p = list(accumulate(a))

for i in range(n):
    p[i] %= m
    
c = collections.Counter(p)
ans = 0

for k , v in c.items():
    ans += v*(v-1)//2
    if k == 0:
        ans += v
print(ans)