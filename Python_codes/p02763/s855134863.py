class SegTree():
    def __init__(self, lists, function, basement):
        self.n = len(lists)
        self.K = (self.n-1).bit_length()
        self.func = function
        self.basement = basement
        self.seg = [basement]*(2**(self.K+1))
        X=2**self.K
        for i,v in enumerate(lists):
            self.seg[i+X-1] = v

        for i in range(2*X-2, 0, -2):
            self.seg[(i-1)>>1] = self.func(self.seg[i], self.seg[i-1])

    def update(self, k, value):

        X=2**self.K
        k += X-1
        self.seg[k] = value
        while k:
            k = (k-1)>>1
            self.seg[k] = self.func(self.seg[(k<<1)+1], self.seg[(k<<1)+2])

            

    def query(self, p, q):
        if q <= p:
            return self.basement
        num = 2**self.K
        p += num-1
        q += num-2
        res = self.basement
        while q-p > 1:
            if p & 1 == 0:
                res = self.func(res, self.seg[p])
            if q & 1 == 1:
                res = self.func(res, self.seg[q])
                q -= 1
            p = p>>1
            q = (q-1)>>1
        if p == q:
            res = self.func(res, self.seg[p])
        else:
            res = self.func(self.func(res, self.seg[p]), self.seg[q])
        return res

import sys
input=sys.stdin.readline

N=int(input())
S=list(input())
Q=int(input())
que=[tuple(input().split()) for i in range(Q)]
alpha="abcdefghijklmnopqrstuvwxyz"
Data={alpha[i]:[0]*N for i in range(26)}
for i in range(N):
    Data[S[i]][i]+=1
SEG={alpha[i]:SegTree(Data[alpha[i]],max,0) for i in range(26)}
for X,u,v in que:
    if X=="1":
        u=int(u)-1
        NOW=S[u]
        S[u]=v
        SEG[NOW].update(u,0)
        SEG[v].update(u,1)
    else:
        u,v=int(u)-1,int(v)-1
        res=0
        for j in range(26):
            res+=SEG[alpha[j]].query(u,v+1)
        print(res)
            
        
    
    
