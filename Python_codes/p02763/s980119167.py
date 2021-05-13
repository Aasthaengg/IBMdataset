class SegmentTree(object):  # 1-indexed
    def __init__(self, size, S):
        self.len = 1 << size.bit_length()

        self.array = [0] * (2 * self.len)
        for i, s in enumerate(S):
            self.array[i + self.len] = 1 << (ord(s) - ord('a'))
        for i in range(self.len - 1, 0, -1):
            self.array[i] = self.array[i * 2] | self.array[i * 2 + 1]

    def query1(self, i, x):
        i += self.len
        self.array[i] = 1 << (ord(x) - ord('a'))
        i >>= 1
        while i > 0:
            self.array[i] = self.array[i * 2] | self.array[i * 2 + 1]
            i >>= 1

    def get(self, i):
        return self.array[i + self.len]

    def query(self, l, r, i, a, b):
        if l == a and r == b:
            return self.array[i]
        center = (a + b) // 2
        if center >= r:
            return self.query(l, r, i * 2, a, center)
        elif center <= l:
            return self.query(l, r, i * 2 + 1, center, b)
        else:
            return self.query(l, center, i * 2, a, center) | self.query(center, r, i * 2 + 1, center, b)

    def query2(self, l, r):
        ans = self.query(l - 1, r, 1, 0, self.len)
        print(bin(ans).count('1'))


N = int(input())
S = input()
tree = SegmentTree(N, S)
Q = int(input())

for _ in range(Q):
    a, b, c = map(str, input().split())
    if a == "1":
        b = int(b)
        tree.query1(b-1, c)
    else:
        b = int(b)
        c = int(c)
        tree.query2(b, c)
