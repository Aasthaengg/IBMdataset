# E - Simple String Queries

class FenwickTree():
    
    # インデックスは1-start
    # 初期化
    def __init__(self, n):
        self.n = n
        self.data = [0]*(n+1)
        self.el = [0]*(n+1)
    
    # private function
    def summation(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s
    
    # i番目の要素にxを加える（初期値 0）
    def add(self, i, x):
        self.el[i] += x
        while i <= self.n:
            self.data[i] += x
            i += i & -i
    
    # i番目の要素 or [i,j]の要素和を取得
    def get(self, i, j=None):
        if j is None:
            return self.el[i]
        return self.summation(j) - self.summation(i-1)

N = int(input())
S_raw = input()
S = [0]*(N+1)
trees = [FenwickTree(N) for _ in range(26)]
for i in range(1,N+1):
    s = S_raw[i-1]
    S[i] = s
    k = ord(s)-ord('a')
    trees[k].add(i, 1)

Q = int(input())
for _ in range(Q):
    q,x,y = input().split()
    if q=='1':
        i,c = int(x),y
        s = S[i]
        k = ord(s)-ord('a')
        trees[k].add(i, -1)
        S[i] = c
        k = ord(c)-ord('a')
        trees[k].add(i, 1)
    else:
        l,r = int(x),int(y)
        ans = 0
        for k in range(26):
            ans = ans+1 if trees[k].get(l,r)>0 else ans
        print(ans)