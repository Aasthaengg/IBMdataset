N, M = map(int, input().split())
P = tuple(map(int, input().split()))
A = []
for _ in range(M):
    i, k = map(int, input().split())
    A.append((i-1, k-1))
class Union():
    def __init__(self, n):
        self.para = [-1] * n
    
    def find(self, n):
        if self.para[n] < 0:
            return n
        
        else:
            self.para[n] = self.find(self.para[n])
            return self.para[n]
    
    def union(self, n, m):
        n = self.find(n)
        m = self.find(m)
        if n == m:
            return False
        else:
            if self.para[n] > self.para[m]:
                n, m = m, n
            
            self.para[n] += self.para[m]
            self.para[m] = n
    
    def same(self, n, m):
        return self.find(n) == self.find(m)
ut = Union(N)
for i,k in A:
    ut.union(i, k)
for i in range(N):
    ut.find(i)

cnt = 0
for i in range(N):
    if P[i] == i + 1:
        cnt += 1
    else:
        if ut.same(P[i]-1, i):
            cnt += 1
print(cnt)