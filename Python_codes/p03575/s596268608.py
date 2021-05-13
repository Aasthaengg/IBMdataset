class UnionFind():
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.height = [0]*n

    def get_root(self, i):
        if self.parent[i] == i:
            return i
        else:
            self.parent[i] = self.get_root(self.parent[i])
            return self.parent[i]
        
    def unite(self, i, j):
        root_i = self.get_root(i)
        root_j = self.get_root(j)
        if root_i != root_j:
            if self.height[root_i] < self.height[root_j]:
                self.parent[root_i] = root_j
            else:
                self.parent[root_j] = root_i
                if self.height[root_i] == self.height[root_j]:
                    self.height[root_i] += 1
    
    def is_in_group(self, i, j):
        if self.get_root(i) == self.get_root(j):
            return True
        else:
            return False



def main():
    import sys

    def input(): return sys.stdin.readline().rstrip()

    n, m = map(int, input().split())
    edges = []
    for i in range(m):
        a, b = map(int, input().split())
        edges.append((a-1, b-1))
    
    cnt = 0
    for i in range(m):
        uf = UnionFind(n)
        for j in range(m):
            if i == j: continue
            a, b = edges[j]
            uf.unite(a, b)
        flag = 1
        for j in range(n):
            flag &= uf.is_in_group(0, j)
        if not flag: 
            cnt += 1
    print(cnt)
            
                
if __name__ == '__main__':
    main()