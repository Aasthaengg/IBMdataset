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
cs = np.array(count).cumsum()
block = len(count)
if S[0] == '0':
    zeros = int(np.ceil(block/2))
    if K >= zeros:
        print(len(S))
    else:
        m = cs[K*2-1]
        if S[-1] == '1':
            for i in range(1,zeros-K+1):
                m = max(m,cs[2*i+2*K-1]-cs[2*(i-1)])
        else:
            for i in range(1,zeros-K):
                m = max(m,cs[2*i+2*K-1]-cs[2*(i-1)])
            m = max(m,cs[-1]-cs[-2*K-1])
        print(m)
else:
    zeros = int(np.floor(block/2))
    if K >= zeros:
        print(len(S))
    else:
        m = cs[2*K]
        if S[-1] == '1':
            for i in range(1,zeros-K+1):
                m = max(m,cs[2*i+2*K]-cs[2*i-1])
        else:
            for i in range(1,zeros-K):
                m = max(m,cs[2*i+2*K]-cs[2*i-1])
            m = max(m,cs[-1]-cs[-2*K-1])
        print(m)