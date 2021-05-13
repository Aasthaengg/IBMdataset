a,b=map(int,input().split())
List = []
A = 0
for i in range(1,1000):
  A +=i
  List.append(A)
K = b - a -1
east = List[K]
res = east - b
print(res)