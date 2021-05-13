class Converter:
    d = {
        1: { 2: 3, 3: 5, 4: 2, 5: 4, },
        2: { 1: 4, 3: 1, 4: 6, 6: 3, },
        3: { 1: 2, 2: 6, 5: 1, 6: 5, },
        4: { 1: 5, 2: 1, 5: 6, 6: 2, },
        5: { 1: 3, 3: 6, 4: 1, 6: 4, },
        6: { 2: 4, 3: 2, 4: 5, 5: 3, }
        }

    def __init__(self, s):
        l = s.split()
        self.tbl = dict(zip(l, range(1,7)))
        self.pip = dict(zip(range(1,7), l))

    def __call__(self, s):
        l, r = s.split()
        print(self.pip[self.d[self.tbl[l]][self.tbl[r]]])

cv = Converter(input())
n = int(input())
for _ in range(n):
    cv(input())