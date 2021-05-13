import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

from heapq import heappush, heappop
from collections import defaultdict

N,Q = map(int,readline().split())
data = list(map(int,read().split()))
S = data[:3*N:3]
T = data[1:3*N:3]
X = data[2:3*N:3]
D = data[3*N:]

event = []
event += [(s-x,1,x) for x,s in zip(X,S)] # xに通行止めを1つ追加
event += [(t-x,2,x) for x,t in zip(X,T)] # xの通行止めを1つ削除
event += [(x,3,i) for i,x in enumerate(D)] # 最小の通行止めを答える

event.sort()

INF = 10**10
q = [INF]
counter = defaultdict(int)
counter[INF] = 1

answer = [None] * Q
for a,b,c in event:
    if b == 1:
        heappush(q,c)
        counter[c] += 1
    elif b == 2:
        counter[c] -= 1
    else:
        while counter[q[0]] == 0:
            heappop(q)
        x = q[0]
        if x == INF:
            x = -1
        answer[c] = x

print('\n'.join(map(str,answer)))