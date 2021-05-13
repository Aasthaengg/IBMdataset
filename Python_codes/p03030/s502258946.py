N=int(input())
d={}
k=[]
for x in range(N):
  S,P=input().split()
  if S not in k:
    k.append(S)
    d[S]=[]
  d[S].append([int(P),x+1])
k.sort()
for y in k:
  d[y].sort(reverse=True)
  for z in range(len(d[y])):
    print(d[y][z][1])