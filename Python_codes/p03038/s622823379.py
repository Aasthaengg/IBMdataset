"""
カードの中から値がC未満のものをB枚までCに変更していく。これを高速に行えばよい。
heapqにぶち込めばよさそう?いや、それだとO(NMlogN)かかる
BIT使えばよいのか？いや、それもダメO(10**9log10**9)かかる
1クエリに対して、logN以下で処理しなくてはいけない。
Aを昇順に並べ替えておいて、常に昇順が保たれるようにしておけば二分探索できる。
あーでも途中で値を更新する作業があるから結局O(MN)かかるな
そもそも値を配列で管理してはいけないんだな。
どの値がいくつある。という管理の仕方をしないといけない。
ってなると、座標圧縮してBITだな。これはムズイわ。
"""
class BIT:
    def __init__(self,n):
        self.tree = [0]*(n+1)
        self.size = n

    def sum(self,i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i&-i
    
    def add(self,i,x):
        while i <= self.size:
            self.tree[i] += x
            i += i&-i

import heapq
N,M = map(int,input().split())
A = list(map(int,input().split()))
heapq.heapify(A)
BC = [list(map(int,input().split())) for _ in range(M)]
BC.sort(key=lambda x: -x[1])

for b,c in BC:
    while b > 0:
        b -= 1
        a = heapq.heappop(A)
        if a < c:
            heapq.heappush(A,c)
        else:
            heapq.heappush(A,a)
            break
    else:
        continue
    break
print(sum(A))
