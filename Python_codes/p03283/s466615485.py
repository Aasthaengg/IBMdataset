n, m, Q = map(int, input().split())

class Cumulative_Sum_2D:
    def __init__(self, a):
        lai = len(a)
        laj = len(a[0])
        self.s = [[0] * (laj + 1) for _ in range(lai + 1)]
        for i in range(lai):
            for j in range(laj):
                self.s[i+1][j+1] = self.s[i+1][j] + a[i][j]
        for i in range(lai):
            for j in range(laj):
                self.s[i+1][j+1] += self.s[i][j+1]
    def sum(self, li, lj, ri, rj):
        s = self.s
        return s[ri][rj] - s[li][rj] - s[ri][lj] + s[li][lj]

a = [[0] * n for _ in range(n)]
for _ in range(m):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    a[l][r] += 1

cs = Cumulative_Sum_2D(a)

for _ in range(Q):
    p, q = map(int, input().split())
    p -= 1
    q -= 1
    print(cs.sum(p,p, q+1,q+1))
