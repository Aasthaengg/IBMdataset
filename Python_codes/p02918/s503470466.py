from collections import deque
import numpy as np
N,K = (int(x) for x in input().split())
S = input()
count = []
d = deque(list(S))

now = d.popleft()
cum = 1
for i in range(len(S)-1):
    popped = d.popleft()
    if popped == now:
        cum += 1
    else:
        count.append(cum)
        now = popped
        cum = 1
count.append(cum)
points = [i-1 for i in count]
cs1 = np.array(count).cumsum()
cs2 = np.array(points).cumsum()

if len(count) // 2 <= K:
    print(N-1)
else:
    m = 0
    for i in range(len(count)-2*K):
        if i == 0:
            c = cs1[2*K] - 1
            d = cs2[-1] - cs2[2*K]
        elif i == len(count) - 2*K + 1:
            c = cs1[-1] - cs1[-2*K-2] - 1
            d = cs2[-2*K-2]
        else:
            c = cs1[2*K+i] - cs1[i-1] - 1
            d = cs2[i-1] + (cs2[-1]-cs2[2*K+i])
        m = max(m,c+d)
    print(m)