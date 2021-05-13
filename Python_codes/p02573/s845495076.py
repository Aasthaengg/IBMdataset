class Union:
    def __init__(self, number):
        self.__number = number
        self.parentList = [-1] * number
 
    def getNumber(self):
        return self.__number 

    def getRoot(self, index):
        if self.parentList[index] < 0:
            return index
        root = self.getRoot(self.parentList[index])
        self.parentList[index] = root
        return root
      
    def unite(self, i, j):
        i = self.getRoot(i)
        j = self.getRoot(j)
        if i != j:
            if i > j:
                i, j = j, i
            self.parentList[i] += self.parentList[j]
            self.parentList[j] = i
 
    def getSize(self, i):
        return -self.parentList[self.getRoot(i)]
 
n, m = map(int, input().split())
 
friendUnion = Union(n)
for i in range(m):
  a, b = map(int, input().split())
  friendUnion.unite(a-1, b-1)
 
unionSizes = [friendUnion.getSize(i) for i in range(friendUnion.getNumber())]
print(max(unionSizes))