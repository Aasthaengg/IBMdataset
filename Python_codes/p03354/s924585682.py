import sys
input=sys.stdin.readline
def main():
  n,m=map(int,input().split())
  p=list(map(int,input().split()))
  xy=[list(map(int,input().split())) for i in range(m)]
  class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)
  uf=UnionFind(n)
  for i in range(m):
    uf.union(p[xy[i][0]-1]-1,p[xy[i][1]-1]-1)
  ans=0
  for i in range(n):
    if uf.same(i,p[i]-1):
      ans+=1
  print(ans)
if __name__=='__main__':
  main()
