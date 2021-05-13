class BIT:
    def __init__(self, n):
        self.n = n
        self.data = [0] * (n + 1)

    def total(self, i):
        res = 0
        while i:
            res += self.data[i]
            i -= i & -i
        return res

    def add(self, i, val):
        while i <= self.n:
            self.data[i] += val
            i += i & -i


N = int(input())
bit = BIT(N)
for i, c in enumerate(input()):
    ind = ord(c) - ord("a")
    bit.add(i + 1, 1 << (ind * 20))
Q = int(input())
for _ in range(Q):
    parts = input().split()
    if parts[0] == "1":
        ind = int(parts[1])
        nval = 1 << ((ord(parts[2]) - ord("a")) * 20)
        val = bit.total(ind) - bit.total(ind - 1)
        bit.add(ind, nval - val)
    else:
        l, r = map(int, parts[1:])
        val = bit.total(r) - bit.total(l - 1)
        mask = (1 << 20) - 1
        ans = 0
        while val:
            if val & mask:
                ans += 1
            val >>= 20
        print(ans)
