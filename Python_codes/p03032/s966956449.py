from collections import deque
import heapq
def f(d,n):
    a = list(d)
    heapq.heapify(a)
    while n > 0 and len(a) > 0:
        tmp = heapq.heappop(a)
        if tmp >= 0:
            heapq.heappush(a,tmp)
            break
        n -= 1
    return sum(a)
#マイナスを取り除いて和を求める関数をあらかじめ作っておく
#優先度付きキューを使うと楽
N, K = map(int, input().split())
V = list(map(int, input().split()))
ans = 0
for i in range(1,min(N,K)+1):
    d = deque()
    for k in range(i):
        d.append(V[k])
    ans = max(ans,f(d,K-i))
    for k in range(i):
        d.pop()
        d.appendleft(V[N-1-k])
        ans = max(ans,f(d,K-i))
print(ans)
#解説中のa+b,bについてループで全探索している
