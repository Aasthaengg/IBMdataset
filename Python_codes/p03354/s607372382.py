n,m = map(int,input().split())
p_list = list(map(int,input().split()))
x_y_list = []
for i in range(m):
  x_y_list.append(list(map(int,input().split())))
  
class UnionFindPathCompression():
    def __init__(self, n):
        self.parents = list(range(n))

    def find(self, x):
        if self.parents[x] == x:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        self.parents[y] = x
        
    def same(self, x, y):
        return self.find(x) == self.find(y)
U = UnionFindPathCompression(n)

for x_y in x_y_list:
  x = x_y[0] -1
  y = x_y[1] - 1
  U.union(x,y)
  
count = 0
for i in range(n):
  if U.same(i,p_list[i]-1) == True:
    count += 1
    
print(count)