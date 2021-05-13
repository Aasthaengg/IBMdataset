import collections
import sys
sys.setrecursionlimit(10**7)

N,K = list(map(int,input().split()))
h = list(map(int,input().split()))

dq = collections.deque([0])

for i in range(1,N):
    l = []
    if i<K+1:
        for k in range(1,i+1):
            l.append(dq[i-k]+abs(h[i]-h[i-k]))

        dq.append(min(l))
    else:
        for k in range(1,K+1):
            l.append(dq[k]+abs(h[i]-h[i-K+k-1]))
        dq.append(min(l))
        dq.popleft()
print(dq.pop())