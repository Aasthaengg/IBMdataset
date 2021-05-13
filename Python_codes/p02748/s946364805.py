A,B,M=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
nooff=sorted(a)[0]+sorted(b)[0]
withoff=[]
for i in range(M):
  x,y,c=map(int,input().split())
  off=a[x-1]+b[y-1]-c
  withoff.append(off)
print(min(sorted(withoff)[0],nooff))