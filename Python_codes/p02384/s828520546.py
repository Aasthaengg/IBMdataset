class Dice:
    D = {'E':(3,1,0,5,4,2), 'W':(2,1,5,0,4,3), 'S':(4,0,2,3,5,1), 'N':(1,5,2,3,0,4)}
    def __init__(self, tp, fwd, rs, ls, bk, bm):
        self.nbrs = [tp, fwd, rs, ls, bk, bm]
        self.RS = [[0, rs, bk, fwd, ls, 0], [ls, 0, tp, bm, 0, rs], [fwd, bm, 0, 0, tp, bk], [bk, tp, 0, 0, bm, fwd],
              [rs, 0, bm, tp, 0, ls], [0, ls, fwd, bk, rs, 0]]
    def rll(self, drctn):
        return [self.nbrs[i] for i in self.D[drctn]]
    def rs(self,tp,fwd):
        return self.RS[tp][fwd]


A = input().split()
dice = Dice(A[0], A[1], A[2], A[3], A[4], A[5])
for _ in range(int(input())):
    tp, fwd = input().split()
    print(dice.rs(dice.nbrs.index(tp), dice.nbrs.index(fwd)))
