import sys


class SegmentTree():
    """
    update, get を提供するSegmentTree

    Attributes
    ----------
    __n : int
        葉の数。2 ^ i - 1
    __dot :
        Segment function
    __e: int
        単位元
    __node: list
        Segment Tree
    """
    def __init__(self, A, dot, e):
        """
        Parameters
        ----------
        A : list
            対象の配列
        dot :
            Segment function
        e : int
            単位元
        """
        n = 2 ** (len(A) - 1).bit_length()
        self.__n = n
        self.__dot = dot
        self.__e = e
        self.__node = [e] * (2 * n)
        for i in range(len(A)):
            self.__node[i + n] = A[i]
        for i in range(n - 1, 0, -1):
            self.__node[i] = self.__dot(self.__node[2 * i], self.__node[2 * i + 1])
    
    def update(self, i, c):
        i += self.__n
        node = self.__node
        node[i] = c
        while i > 1:
            i //= 2
            node[i] = self.__dot(node[2 * i], node[2 * i + 1])

    def get(self, l, r):
        vl, vr = self.__e, self.__e
        l += self.__n
        r += self.__n
        while (l < r):
            if l & 1:
                vl = self.__dot(vl, self.__node[l])
                l += 1
            l //= 2
            if r & 1:
                r -= 1
                vr = self.__dot(vr, self.__node[r])
            r //= 2
        return self.__dot(vl, vr)


N, C = map(int, input().split())
S = [tuple(map(int, s.split())) for s in sys.stdin.readlines()]

R = [0] * (N + 1)
pos = 0
for i, (x, v) in enumerate(S):
    R[i + 1] = R[i] + v - (x - pos)
    pos = x
L = [0] * (N + 1)
pos = 0
for i, (x, v) in enumerate(reversed(S)):
    x = C - x
    L[i + 1] = L[i] + v - (x - pos)
    pos = x

RST = SegmentTree(R, max, 0)
LST = SegmentTree(L, max, 0)
ans1 = RST.get(0, N + 1)
ans2 = LST.get(0, N + 1)

score = 0
pos = 0
ans3 = 0
for i in range(N):
    x, v = S[i]
    score += v - (x - pos) * 2
    ans3 = max(ans3, score + LST.get(0, N - i))
    pos = x

score = 0
pos = 0
ans4 = 0
for i in range(N):
    x, v = S[N - 1 - i]
    x = C - x
    score += v - (x - pos) * 2
    ans4 = max(ans4, score + RST.get(0, N - i))
    pos = x


print(max([ans1, ans2, ans3, ans4]))
