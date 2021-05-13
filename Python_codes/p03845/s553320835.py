N=int(input())
tlist=list(map(int,input().split()))
M=int(input())

tsum=sum(tlist)
pxlist=[]
for i in range(M):
  p,x=map(int,input().split())
  print(tsum-(tlist[p-1]-x))