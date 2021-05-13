"""
愚直に一人一人交通止めに対してシミュレートしていは、絶対に間に合わない。

そこで、「この時間に出発したら"まず最初に"この通行止めで引っかかる」というのを前処理でまとめておく。
これは座標圧縮とセグメント木っぽいものを用いることで実現可能。
"""
N,Q = map(int,input().split())
STX = [list(map(int,input().split())) for _ in range(N)]
D = [int(input()) for _ in range(Q)]
times = set(D+[s-x for s,t,x in STX]+[t-x for s,t,x in STX])
compTimes = {t:i for i,t in enumerate(sorted(times))}

class originalSegTree:
    def __init__(self,n):
        self.end_leaves = 2**n.bit_length()
        self.tree = [float("INF")]*(2*self.end_leaves)
    
    def add(self,left,right,x):
        L = left + self.end_leaves
        R = right + self.end_leaves
        while L < R:
            if L&1:
                self.tree[L] = min(self.tree[L],x)
                L += 1
            if R&1:
                R -= 1
                self.tree[R] = min(self.tree[R],x)
            L >>= 1
            R >>= 1
    
    def merge(self):
        for i in range(1,self.end_leaves):
            self.tree[i*2] = min(self.tree[i],self.tree[i*2])
            self.tree[i*2+1] = min(self.tree[i],self.tree[i*2+1])

seg = originalSegTree(len(compTimes))
for s,t,x in STX:
    a = compTimes[s-x]
    b = compTimes[t-x]
    seg.add(a,b,x)

seg.merge()

for d in D:
    c = compTimes[d]
    ans = seg.tree[c+seg.end_leaves]
    if ans == float("INF"):
        ans = -1
    print(ans)
