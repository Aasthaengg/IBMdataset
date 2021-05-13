r,c=map(int,input().split())
C=[]
for _ in range(r):
  ns = list(map(int, input().split()))
  ns.append(sum(ns))
  C.append(ns)
#print(C)
R = list(zip(*C))
#print(R)
C.append([sum(x) for x in R])
for r in C:
  print(*r)
