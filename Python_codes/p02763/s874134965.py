import sys
input = sys.stdin.readline

class SegmentTree():
    def segfunc(self, x, y):
        return max(x, y)
        
    def __init__(self, ide_ele, n, l, target):
        # n以上の最小の2のべき乗、一番下の段はここからスタートになる
        self.ide_ele = ide_ele
        self.num =2**(n-1).bit_length()
        self.tree = [ide_ele]*self.num*2
        # 一番下の段
        for i in range(n):
            if l[i] == target:
                self.tree[i+self.num-1] = 1
        # 
        for i in range(self.num-2, -1, -1):
            self.tree[i] = self.segfunc(self.tree[2*i+1], self.tree[2*i+2])
    
    def update(self, k, add):
        k += self.num-1
        if add:
            self.tree[k] = 1
        else:
            self.tree[k] = 0
        while k:
            k = (k-1)//2
            self.tree[k] = self.segfunc(self.tree[k*2+1], self.tree[k*2+2])
    
    def query(self, p, q):
        if q<=p:
            return self.ide_ele

        # [p, q)
        p += self.num - 1
        q += self.num - 2
        res = self.ide_ele
        while q-p>1: # まだ隣同士の節点ではないなら
            # &で偶奇判定->中途半端な位置にいるなら寄せる
            if p&1 == 0: #左なのに右端
                res = self.segfunc(res, self.tree[p])
            if q&1 == 1: #右なのに左端
                res = self.segfunc(res, self.tree[q])
                q -= 1
            p = p//2
            q = (q-1)//2
        if p==q:
            res = self.segfunc(res, self.tree[p])
        else:
            res = self.segfunc(self.segfunc(res, self.tree[p]), self.tree[q])
        return res

    # 閉区間になってる
    def rec_query(self, p, q, k, l, r):
        #q -= 1 [)の場合
        #print(p, q, k, l, r)
        if r < p or q < l: # out of range
            return self.ide_ele
        if p <= l and r <= q:
            return self.tree[k]
        else:
            vl = self.rec_query(p, q, k*2+1, l, (l+r)//2)
            vr = self.rec_query(p, q, k*2+2, (l+r)//2+1, r)
        #print(vl, vr)
        return self.segfunc(vl, vr)



N = int(input())
S = input()
Q = int(input())

result = ""

d = {}
for i in range(26):
    d[chr(ord("a")+i)] = SegmentTree(0, N, S, chr(ord("a")+i))

S = list(S)

for q in range(Q):
    case, p, q = (i for i in input().split())
    #print(case, p, q)
    p = int(p)-1
    case = int(case)
    if case==1:
        #print(p)
        d[S[p]].update(p, False)
        d[q].update(p, True)
        S[p] = q
    else:
        ans = 0
        for c in range(26):
            #print(d[chr(ord("a")+c)].tree)
            ans += d[chr(ord("a")+c)].query(p, int(q))
        result += str(ans)+"\n"

#print(S)
print(result[:-1])
