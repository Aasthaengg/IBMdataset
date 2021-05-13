from collections import defaultdict
from bisect import bisect_left
s = input()
t = input()
d = defaultdict(list)

ls = len(s)
cnt = 0

for ind,i in enumerate(s):
    d[i].append(ind)
        
if not set(s) >= set(t):
    print(-1)
else:
    now = -1
    for i in t:
        arr = d[i]
        y = (now+1) % ls
        ind = bisect_left(arr, y)
    
        if ind >= len(arr):
            now = now+1 + ls - y + arr[0]
            
        else:
            now = now+1 - y + arr[ind]
    print(now+1)