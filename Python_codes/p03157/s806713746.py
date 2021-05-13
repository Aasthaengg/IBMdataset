from collections import defaultdict


class UnionFind:
    def __init__(self, node):
        self.parent = [-1 for _ in range(node)]
        self.node = node

    def find(self, target):
        if self.parent[target] < 0:
            return target
        else:
            self.parent[target] = self.find(self.parent[target])
            return self.parent[target]

    def is_same(self, x, y):
        return self.find(x) == self.find(y)

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        if self.parent[root_x] > self.parent[root_y]:
            root_x, root_y = root_y, root_x
        self.parent[root_x] += self.parent[root_y]
        self.parent[root_y] = root_x

    def get_size(self, x):
        return -self.parent[self.find(x)]

    def get_root(self):
        return [i for i, root in enumerate(self.parent) if root < 0]

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.node) if self.find(i) == root]

    def all_group_members(self):
        return {r: self.members(r) for r in self.get_root()}


def main():
    h, w = map(int, input().split())
    grid = [["*" for _ in range(w + 2)]]
    for _ in range(h):
        grid.append(["*"] + list(input()) + ["*"])
    grid.append(grid[0])
    uf = UnionFind(h * w)
    all_black = []

    def grid_num(i, j):
        return w * (i - 1) + j - 1

    for i in range(1, h + 1):
        for j in range(1, w + 1):
            for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                ni = i + di
                nj = j + dj
                if grid[ni][nj] == "*":
                    continue
                elif grid[i][j] != grid[ni][nj]:
                    uf.union(grid_num(i, j), grid_num(ni, nj))
            if grid[i][j] == "#":
                all_black.append([i, j])
    ans = 0

    black = defaultdict(int)
    for i, j in all_black:
        black[uf.find(grid_num(i, j))] += 1
    for i, r in enumerate(uf.parent):
        if r < 0:
            ans += black[i] * (-r - black[i])
    print(ans)


if __name__ == '__main__':
    main()
