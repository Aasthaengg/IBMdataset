n=int(input())
d={}
l=[]
for i in range(n):
  s=input()
  if s not in d:
    d[s]=1
  else:
    d[s]=d[s]+1
k=max(d.values())
for i,j in d.items():
  if j==k:
    l.append(i)
l.sort()
for i in range(len(l)):
  print(l[i])