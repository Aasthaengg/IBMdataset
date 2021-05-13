from collections import defaultdict
import sys
sys.setrecursionlimit(1000000)
def main():
    class Tree():
        def __init__(self, n, root, connects):
            self._root = root
            self._connects = connects
            self._parents = [0] * n
            self._parents[root] = None
            self._children = [0] * n
            self._children[self._root] = connects[self._root]
            self.make_tree(self._root)

        def make_tree(self, node):
            for child in self._children[node]:
                self._parents[child] = node
                self._children[child] = [c for c in self._connects[child] if c != node]
                if self._children[child] != []:
                    self.make_tree(child)

        def parents(self, node):
            return self._parents[node]

        def children(self, node):
            return self._children[node]

    def add_subtree(i):
        for c in t.children(i):
            ans[c] += ans[i]
            add_subtree(c)

    n, q = map(int, input().split())
    G = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(lambda x: int(x) - 1, input().split())
        G[a].append(b)
        G[b].append(a)
    t = Tree(n, root = 0, connects = G)
    ans = [0] * n
    for _ in range(q):
        p, x = map(int, input().split())
        ans[p - 1] += x
    add_subtree(0)
    print(' '.join(list(map(str, ans))))

if __name__ == '__main__':
    main()
