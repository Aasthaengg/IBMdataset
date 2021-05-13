from collections import defaultdict


class DisjointSet:

    def __init__(self, N):
        self.parents = [i for i in range(N)]
        self.count = N

    def find(self, x):
        path = []
        while self.parents[x] != x:
            x = self.parents[x]
            path.append(x)
        for p in path:
            self.parents[p] = x
        return x

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if self.find(root_x) != self.find(root_y):
            self.parents[root_x] = root_y
            self.count -= 1


def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def read_oneless_ints():
    return [int(a)-1 for a in input().strip().split(' ')]


def solve():
    N, K, L = read_ints()
    disjoint_set_roads = DisjointSet(N)
    disjoint_set_railways = DisjointSet(N)

    for _ in range(K):
        u, v = read_oneless_ints()
        disjoint_set_roads.union(u, v)
    for _ in range(L):
        u, v = read_oneless_ints()
        disjoint_set_railways.union(u, v)
    G = defaultdict(list) # (p1, p2) -> [nodes]
    for i in range(N):
        G[(disjoint_set_roads.find(i), disjoint_set_railways.find(i))].append(i)
    answer = [None]*N
    for city_list in G.values():
        for city in city_list:
            answer[city] = len(city_list)
    for a in answer:
        print(a)


if __name__ == '__main__':
    solve()
