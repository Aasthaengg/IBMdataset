k,s = map(int,input().split())
ans = 0

from itertools import product
for x,y in product(range(k+1), repeat=2):
    if 0 <= s-x-y <= k:
        ans +=1
print(ans)
