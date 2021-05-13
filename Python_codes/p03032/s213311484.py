n, k = map(int, input().split())
V = list(map(int, input().split()))

from collections import deque
V = deque(V)

import copy

ans = -10**18
for i in range(k+1):
    for j in range(k+1):
        if i+j > k:
            continue
        if i+j > n:
            continue
        V_ = copy.copy(V)
        temp = []
        for p in range(i):
            temp.append(V_.popleft())
        for q in range(j):
            temp.append(V_.pop())
        temp.sort()
        s = sum(temp)
        l = k-i-j
        for r in range(min(l, len(temp))):
            if temp[r] < 0:
                s -= temp[r]
        ans = max(ans, s)
print(ans)
