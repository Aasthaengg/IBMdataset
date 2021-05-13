n, m = map(int, input().split())
fset = set([i for i in range(1, m + 1)])
allset = fset
for i in range(n):
  temp = set(list(map(int, input().split()))[1:])
  fset = fset - (allset - temp)
print(len(fset))