ns=[]

for i in range(4):
  ns.append(input())

n=[]

for j in range(4):
  n.append(int(ns[j]))

if n[0]<=n[1]:
  print(n[2]*n[0])
else:
  print(n[2]*n[1]+n[3]*(n[0]-n[1]))