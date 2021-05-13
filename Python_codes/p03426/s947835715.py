#ABC089-D Practical Skill Test
"""
全てのクエリをO(1)で求められるようにメモ化すればok
1~H*Wの数字がどのマスに書いてあるのかを求める。(数字→座標を調べられるようにする)
そうしたときに、D個前のコストを足し合わせる累積和という方法を用いて各クエリO(1)で求められるようになる
"""
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

h,w,d = map(int,readline().split())
A = []
for i in range(h):
    A.append(list(map(int,readline().split())))

cor = [[] for _ in range(h*w)]
for i,a in enumerate(A):
    for j,b in enumerate(a):
        cor[b-1] = [i,j]

cost = [0]*(h*w)
for i in range(h*w):
    if i < d:
        continue
    cost[i] = cost[i-d] + abs(cor[i-d][0]-cor[i][0]) + abs(cor[i-d][1]-cor[i][1])


q = int(readline())
for i in range(q):
    l,r = map(int,readline().split())
    l,r = l-1,r-1
    res = cost[r]-cost[l]
    print(res)