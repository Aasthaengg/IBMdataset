A,B,N=list(map(int,input().split()))
listA=list(map(int,input().split()))
listB=list(map(int,input().split()))
ma=sorted(listA)
mb=sorted(listB)
M=min(ma)+min(mb)
for i in range(N):
  x,y,c=list(map(int,input().split()))
  ans=listA[x-1]+listB[y-1]-c
  if ans<M:
    M=ans
print(M)