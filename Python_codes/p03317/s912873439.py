import math
n,k = map(int,input().split())
a = list(map(int,input().split()))
m = a.index(1)
ans = 9999999999
left = len(a[:m])
right = len(a[m:])
for i in range(k):
    x = left  - i
    y = right - (k-i)
    if x < 0 or y < 0:
        continue
    count = 1 + math.ceil(x/(k - 1)) + math.ceil(y/(k - 1))
    ans = min(ans,count)
print(ans)