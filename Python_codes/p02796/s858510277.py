N=int(input())
INF=10**20
 
X=[]
for i in range(N):
  x,l=map(int,input().split())
  X.append((x-l,x+l-1))
  
X = sorted(X,key=lambda x:x[1])

last=0
ans=1
for i in range(1,N):
  if X[last][1]<X[i][0]:
    ans += 1
    last=i
  else:
    continue
    
print(ans)