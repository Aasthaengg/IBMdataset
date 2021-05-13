class BisectSearch:
    def __init__(self, f, l=0, r=10**9):
        self.f = f
        self.l = l
        self.r = r
    def __call__(self, dist):
        f = self.f
        l = self.l
        r = self.r
        if dist <= f(l):
            return l
        if f(r) <= dist:
            return r
        while r-l > 1:
            n = (r+l) // 2
            if f(n) <= dist:
                l = n
            else:
                r = n
        return l

n = int(input())
def f(n):
    return (n+1)*n // 2
m = BisectSearch(f, l=1, r=10**7)(n)
m += f(m) != n
A = set()
for i in range(m, 0, -1):
  if n - i >= 0:
    A.add(i)
    n -= i
print(*A, sep='\n')