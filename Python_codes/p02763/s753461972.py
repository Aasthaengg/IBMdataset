n, s, q = int(input()), input(), int(input())

class SegmentTree:
    def __init__(self, n, func=lambda x, y: min(x, y), ide=float("inf")):
        self.n = 2 ** (n-1).bit_length()
        self.data = [ide] * (self.n*2)
        self.func, self.ide = func, ide
    
    def build(self, data):
        for i, x in enumerate(data):
            self.data[self.n+i] = x
        for i in range(self.n-1, 0, -1):
            self.data[i] = self.func(self.data[i*2], self.data[i*2+1])

    def update(self, i, x):
        i += self.n
        self.data[i] = x
        while i > 1:
            i //= 2
            self.data[i] = self.func(self.data[i*2], self.data[i*2+1])

    def query(self, l, r):
        l += self.n; r += self.n 
        res = self.ide
        while l < r:
            if l & 1:
                res = self.func(res, self.data[l])
                l += 1
            if r & 1:
                res = self.func(res, self.data[r-1])
            l //= 2; r //= 2
        return res
    
    def get(self, i):
        return self.data[self.n + i]

st = [SegmentTree(n, lambda x, y: x+y, 0) for _ in range(26)]
for i, c in enumerate(s): st[ord(c)-97].update(i, 1)

for _ in range(q):
    a, b, c = input().split()
    if a == "1":
        idx = int(b)-1
        for i in range(26):
            st[i].update(idx, 0)
        st[ord(c)-97].update(idx, 1)
    else:
        l, r = int(b)-1, int(c)
        res = 0
        for i in range(26):
            res += bool(st[i].query(l, r))
        print(res)
