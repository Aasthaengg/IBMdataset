h,w,n = map(int, input().split())

from collections import Counter
d = []

for _ in range(n):
    a,b = map(int,input().split())
    for k in range(3):
        for l in range(3):
            if 0 < a-k < h-1 and 0 < b-l < w-1:
                d.append((a-k,b-l))

dd = Counter(d)
ddd = list(dd.values())

ans = [0]*10

for i in range(1,10):
    ans[i] = ddd.count(i)

ans[0] = (h-2)*(w-2) - sum(ans)

for x in ans:
    print(x)