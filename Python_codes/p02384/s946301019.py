# coding=utf-8


class Dice(object):

    def __init__(self, label):
        self.label = label

    def getLabel(self, i):
        return self.label[i - 1]

    def _rotateS(self):
        self.label = [self.getLabel(i) for i in [5, 1, 3, 4, 6, 2]]

    def _rotateN(self):
        self.label = [self.getLabel(i) for i in [2, 6, 3, 4, 1, 5]]

    def _rotateE(self):
        self.label = [self.getLabel(i) for i in [4, 2, 1, 6, 5, 3]]

    def _rotateW(self):
        self.label = [self.getLabel(i) for i in [3, 2, 6, 1, 5, 4]]

    def _spinPos(self):
        self.label = [self.getLabel(i) for i in [1, 4, 2, 5, 3, 6]]

    def _spinNeg(self):
        self.label = [self.getLabel(i) for i in [1, 3, 5, 2, 4, 6]]

    def rotate(self, rotates):
        for r in rotates:
            if r == 'S':
                self._rotateS()
            elif r == 'N':
                self._rotateN()
            elif r == 'E':
                self._rotateE()
            elif r == 'W':
                self._rotateW()
            elif r == 'T':
                self._spinPos()
            elif r == 'B':
                self._spinNeg()

    def match(self, top, front):
        iTop = self.label.index(top) + 1
        topRot = {1: '', 2: 'N', 3: 'W', 4: 'E', 5: 'S', 6: 'SS'}
        self.rotate(topRot[iTop])

        iFront = self.label.index(front) + 1
        frontRot = {2: '', 3: 'B', 4: 'T', 5: 'TT'}
        self.rotate(frontRot[iFront])


def main():
    d = Dice(map(int, raw_input().split()))
    n = input()
    for _ in xrange(n):
        top, front = map(int, raw_input().split())
        d.match(top, front)
        print d.getLabel(3)

if __name__ == '__main__':
    main()