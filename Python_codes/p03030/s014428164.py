n=int(input())
l=[]
for i in range(n):
  s,P=input().split()
  p=int(P)
  l.append([s,-p,i+1])
L=sorted(l)
for i in range(n):
  print(L[i][2])