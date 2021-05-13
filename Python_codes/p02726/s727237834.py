N,X,Y=[int(s) for s in input().split()]
ans=[0 for i in range(N)]
def distance(i,j):
  return min([j-i,abs(j-Y)+abs(i-X)+1])
  
for i in range(1,N):
  for j in range(i+1,N+1):
    d=distance(i,j)
    ans[d]+=1

for i in range(1,N):
  print(ans[i])