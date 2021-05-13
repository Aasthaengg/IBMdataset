import sys
input = sys.stdin.readline
class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
 
    def sum(self, i):
        s = 0
        while i > 0:       
            s += self.tree[i] 
            i -= i & -i       
        return s                            
                                            
    def add(self, i, x):                  
        while i <= self.size:
            self.tree[i] += x  
            i += i & -i
x = "abcdefghijklmnopqrstuvwxyz"
N, = map(int, input().split())
d = dict()
for c in x:
    d[c] = Bit(N+1)

S = list(input().strip())
for i, c in enumerate(S):
    d[c].add(i+1, 1)

Q = int(input())
for _ in range(Q):
    t, a, b = input().split()
    if t == '1':
        i, c = int(a), b
        b = S[i-1]
        S[i-1] = c
        d[b].add(i, -1)
        d[c].add(i, 1)
    else:
        l, r = int(a), int(b)
        rr = 0
        for c in x:
            if d[c].sum(r) - d[c].sum(l-1) > 0:
                rr += 1
        print(rr)
