class SegT():
    def __init__(self, size, origin):
        self.size = 1
        while self.size < size: self.size *= 2
        self.data = [set() for _ in range(self.size * 2 - 1)]
        for i in range(size):
            self.data[i+self.size-1] = origin[i]
        for i in range(self.size-2,-1,-1):
            self.data[i] = self.data[i*2+1] | self.data[i*2+2]

    
    def update(self, i, x):
        i += (self.size - 1)
        self.data[i] = {x}
        while i > 0:
            i = (i - 1) // 2
            self.data[i] = self.data[i*2+1] | self.data[i*2+2]
        
    def get(self, a, b, node=0, l=0, r=-1):
        if r < 0: r = self.size
        if r <= a or b <= l: return set()
        if a <= l and r <= b: return self.data[node]
        vl = self.get(a, b, node*2+1, l, (l+r)//2)
        vr = self.get(a, b, node*2+2, (l+r)//2, r)
        return vl | vr

N = int(input())
S = input()
Q = int(input())
origin = [{i} for i in S]

segt = SegT(N, origin)

for i in range(Q):
    t, l, r = input().split()
    if t == "1":
        segt.update(int(l)-1, r)
    else:
        x = segt.get(int(l)-1,int(r))
        print(len(x))
