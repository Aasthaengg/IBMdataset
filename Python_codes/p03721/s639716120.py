a,b=map(int,input().split())
L=list()
s=0
for i in range(a):
  x,y=map(int,input().split())
  L.append([x,y])
L=sorted(L)
for i in range(a):
  s+=L[i][1]
  if s>=b:
    print(L[i][0])
    break