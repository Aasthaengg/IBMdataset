import sys
from itertools import accumulate
from collections import Counter
from bisect import bisect as br, bisect_left as bl
from operator import itemgetter
class DammyMap:
    #1-indexed
    def __init__(self, A, B):
        #Aに初期状態の要素をすべて入れる,Bは値域のリスト
        #self.X, self.comp = self.compress(B)
        self.X = B[:]
        self.comp = {v : k for k, v in enumerate(D, 1)}
        self.size = len(self.X)
        self.tree = [0] * (self.size + 1)
        self.p = 2**(self.size.bit_length() - 1)
        self.dep = self.size.bit_length()
        
        CA = Counter(A)
        S = [0] + list(accumulate([CA[self.X[i]] for i in range(self.size)]))
        for i in range(1, 1+self.size):
            self.tree[i] = S[i] - S[i - (i&-i)]
        
    def compress(self, L):
        #座圧
        L2 = list(set(L))
        L2.sort()
        C = {v : k for k, v in enumerate(L2, 1)}
        # 1-indexed
        return L2, C
    
    def leng(self):
        #今入っている個数を取得
        return self.count(self.size)
    
    def count(self, i):
        #i(Bの元)以下の個数を取得
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
    
    def less(self, v):
        #v(Bの元である必要はない)未満の個数を取得
        i = bl(self.X, v)
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
    
    def leq(self, v):
        #v(Bの元である必要はない)以下の個数を取得
        i = br(self.X, v)
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
 
    def add(self, i, x):
        #iをx個入れる,負のxで取り出す,iの個数以上取り出すとエラーを出さずにバグる
        i = self.comp[i]
        while i <= self.size:
            self.tree[i] += x
            i += i & -i
        
        
    def get(self, v):
        # v番目の値を取得
        if v <= 0:
            return -1
        s = 0
        k = self.p
        for _ in range(self.dep):
            if s + k <= self.size and self.tree[s+k] < v:
                s += k
                v -= self.tree[s]
            k //= 2
        return self.X[s]

N, Q = map(int, input().split())
stx = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
stx.sort(key = itemgetter(2))
D = [int(sys.stdin.readline()) for _ in range(Q)] 

T = DammyMap(D, D)
ans = [-1]*Q

for s, t, x in stx:
    tl = T.less(s - x)
    tr = T.less(t - x)
    d = tr - tl
    for _ in range(d):
        i = T.get(tl + 1)
        T.add(i, -1)
        ans[T.comp[i]-1] = x
print(*ans, sep = '\n')