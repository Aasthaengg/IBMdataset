class UnionFind:
    Parents = None

    def __init__(self, N):
        self.Parents = [-1 for i in range(N + 1)]

    # Aがどのグループにいるのか調べる
    def root(self, A):
        if self.Parents[A] < 0:
            return A
        else:
            self.Parents[A] = self.root(self.Parents[A])
            return self.Parents[A]

    # Aが所属しているグループのサイズを返す
    def size(self, A):
        return -self.Parents[self.root(A)]

    # AとBをくっつける
    def Connect(self, A, B):
        if self.root(A) == self.root(B):
            return False
        if self.size(A) < self.size(B):
            self.Parents[self.root(B)] += self.Parents[self.root(A)]
            self.Parents[self.root(A)] = B
        else:
            self.Parents[self.root(A)] += self.Parents[self.root(B)]
            self.Parents[self.root(B)] = A
        return True


n, m = map(int, input().split())
a = [input().split() for i in range(m)]
a = [(int(i[0]), int(i[1])) for i in a]
ans = [int(n * (n - 1) / 2) for i in range(m)]
uni = UnionFind(n)

for i in range(m):
    if i == 0:
        continue
    A = a[-i][0]
    B = a[-i][1]

    if uni.root(A) != uni.root(B):
        ans[i] = ans[i-1] - uni.size(A) * uni.size(B)
        uni.Connect(A, B)
    else:
        ans[i] = ans[i-1]


for i in range(1, m+1):
    print(ans[-i])
