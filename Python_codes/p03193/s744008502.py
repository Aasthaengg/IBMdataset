N,H,W=map(int,input().split())
list_1=[[int(i) for i in input().split()] for i in range(N)]
c=0
for i,j in list_1:
  if i>=H and j>=W :
    c=c+1
print(c)