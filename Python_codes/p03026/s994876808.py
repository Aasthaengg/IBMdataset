#M-SOLUTIONS プロコンオープン-D Maximum Sum of Minimum
"""
問題：
木が与えられる。
リストCが与えられるので、各頂点に割り当てる。
全ての辺において、その辺をつなぐ2頂点をa,bとした時、min(Ca,Cb)をスコアとする。
これを最大化するスコアを求め、そのような頂点への数値の割り振りを出力せよ。
考察：
シュミレーションしてみると、
1.辺数が多い頂点に大きい数字を割り当てると良さそう
2.複数あっても適当に選んで良い
3.大きい数字は隣り合ったほうが良い
4.よって、辺数が多い頂点をrootとして、そこから幅を優先して
大きい数字を順に割り当てるのが良さそう。
5.この時には別に子の辺数を気にする必要はない。(これは、その"子"がスコアとして使用
されるのは必ず1回であることから言える)
解法：
接続する辺が最も多い頂点をrootとして、幅優先でそこから大きい値を割り振っていく。
全ての子は必ず1回づつ使われるので、実はスコアの最大値は
all(C)-(rootの値)となる。
"""
import sys
from collections import deque
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
n = int(readline())
g = [[] for _ in range(n)]
edges = [0]*n
for i in range(n-1):
    a,b = map(int,readline().split())
    a,b = a-1,b-1
    edges[a] += 1
    edges[b] += 1
    g[a].append(b)
    g[b].append(a)
C = list(map(int,readline().split()))
C.sort(reverse=True)
C = deque(C)
root = 0
res = 0
for i in range(n):
    if res < edges[i]:
        root = i
        res = edges[i]

ans = [-1]*n
ans[root] = C.popleft()
deq = deque([root])
while deq:
    fr = deq.popleft() #queue
    for go in g[fr]:
        if ans[go] != -1:
            continue
        ans[go] = C.popleft()
        deq.append(go)

print(sum(ans)-ans[root])
print(*ans)