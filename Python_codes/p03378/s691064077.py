N, M, X  = map(int, input().split())
a=[]
for i in input().split():
  a.append(int(i) < X)
  c = a.count(True)
print(min(c, M-c))