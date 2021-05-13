
class BIT:
    def __init__(self, n):
        # 1-indexed
        self.size = n
        self.tree = [0] * (n + 1)

    def sum(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res

    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i


N = int(input())
S = list(input())
Q = int(input())

trees = [BIT(5 * 10 ** 5 + 2) for _ in range(26)]
for i in range(N):
    trees[ord(S[i]) - ord("a")].add(i + 1, 1)

for _ in range(Q):
    s, *x = input().split()
    if s == "1":
        i = int(x[0])
        c = x[1]
        trees[ord(S[i - 1]) - ord("a")].add(i, -1)
        trees[ord(c) - ord("a")].add(i, 1)
        S[i - 1] = c
    else:
        l, r = map(int, x)
        cnt = 0
        for i in range(26):
            cnt += int(trees[i].sum(r) - trees[i].sum(l - 1) > 0)
        print(cnt)
