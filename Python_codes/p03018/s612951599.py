class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.data = [0] * (n + 1)
        self.k_init = 2 ** (self.n - 1).bit_length()

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.n:
            self.data[i] += x
            i += i & -i


def get_invnum(li):
    n = len(li)
    t = FenwickTree(2)
    res = 0
    for i in range(n):
        if li[i] == "A":
            t.add(2, 1)
        else:
            res += t.sum(2)
    return res


S = input()
S = list(S.replace("BC", "D"))
N = len(S)
li = []
ans = 0
for c in S + ["B"]:
    if c not in ("A", "D"):
        ans += get_invnum(li)
        li = []
    else:
        li.append(c)
print(ans)
