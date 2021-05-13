from operator import itemgetter
from itertools import accumulate


n,k = map(int, input().split())
sushi = [list(map(int, input().split())) for i in range(n)]

sushi.sort(key=itemgetter(1))
sushi.reverse()


# 各ネタ最大美味しさの寿司
a = []

# それ以外の寿司
b = []

# aにすでに入っているネタ = 1
in_a = [0]*(n+1)

for i in range(n):
    t,d = sushi[i]
    if in_a[t]==0:
        in_a[t]=1
        a.append(d)
    else:
        b.append(d)

ans = 0

a = list(accumulate([0]+a))
b = list(accumulate([0]+b))


for i in range(len(a)):
    if i<=k:
        if 0<=k-i<len(b):
            ans = max(a[i]+b[k-i]+i**2,ans)
print(ans)