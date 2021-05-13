siz=[0,0,0]
siz=list(map(int,input().split()))
siz=sorted(siz)
if (siz[0]%2==0 or siz[1]%2==0 or siz[2]%2==0):
  print(0)
else:
  print(siz[1]*siz[0])