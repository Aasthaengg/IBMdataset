from typing import Dict, List

N, M = [int(x) for x in input().split()]

class UnionFind:
    def __init__(self, num_node: int):
        self.__parent_index = [x for x in range(num_node)]
        self.__tree_rank = [1] * num_node

    def __is_root(self, index: int) -> bool:
        return self.__parent_index[index] == index

    def root(self, index: int) -> int:
        """Find root index."""
        while not self.__is_root(index):
            index = self.__parent_index[index] = self.root(self.__parent_index[index])
        return index

    def unite(self, x: int, y: int) -> bool:
        """Unite two trees."""
        x = self.root(x)
        y = self.root(y)

        if x == y:
            return False

        if self.__tree_rank[x] < self.__tree_rank[y]:
            x, y = y, x

        self.__tree_rank[x] += self.__tree_rank[y]
        self.__parent_index[y] = x

        return True

    def groups(self) -> Dict[int, List[int]]:
        __groups: Dict[int, List[int]] = {}
        for node, parent in enumerate(self.__parent_index):
            __root = self.root(parent)
            if __groups.get(__root) is None:
                __groups[__root] = [node]
            else:
                __groups[__root].append(node)

        return __groups

uni = UnionFind(N)
for i in range(M):
    a, b = [int(x) - 1 for x in input().split()]
    uni.unite(a, b)

print(len(uni.groups()) - 1)
