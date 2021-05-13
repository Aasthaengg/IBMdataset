n,k=map(int,input().split())
s=input()
r=s.split('L')
r=[i for i in r if i!='']
l=s.split('R')
l=[i for i in l if i!='']
hr=s.count('R')-len(r)
hl=s.count('L')-len(l)
if k>=min(len(r),len(l)):
  print(n-1)
else:
  print(hr+hl+k*2)