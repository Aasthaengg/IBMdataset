node = set([1,2,3,4])
for _ in range(3):
  a,b = map(int,input().split())
  node = node.intersection(set([a,b]))
  
print('NO' if len(node) else 'YES')