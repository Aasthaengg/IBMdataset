from collections import defaultdict
import bisect
S = input()
T = input()

d = defaultdict(list)

for i, s in enumerate(S):
    d[s].append(i)

ans = 0
now = -1
for t in T:
    arr = d[t]
    if len(arr) == 0:
        print(-1)
        exit()
    idx = bisect.bisect_right(arr, now) # leftにすると、同じ文字を2連続探索するときにバグる
    if idx == len(arr):
        ans += 1
        now = arr[0]
    else:
        now = arr[idx]
print(ans * len(S) + now + 1)