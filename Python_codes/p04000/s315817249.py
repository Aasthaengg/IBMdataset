from collections import defaultdict
import sys

input = sys.stdin.readline

h,w,n = map(int,input().split())
d = defaultdict()
ans = [0]*10

for k in range(n):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    for i in range(-1,2):
        for j in range(-1,2):
            if (a+i,b+j) in d:
                d[(a+i,b+j)] += 1
            else:
                d[(a+i,b+j)] = 1

for k,v in d.items():
    if 0 < k[0] < h-1 and 0 < k[1] < w-1:
        ans[v] += 1

ans[0] = (h-2) * (w-2) - sum(ans)

for i in ans:
    print(i)
