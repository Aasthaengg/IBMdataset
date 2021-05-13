N=int(input())
X=[list(map(int,input().split())) for i in range(N)]
def solve(p,q):
  global N,X
  r=0
  for i in range(N):
    for j in range(N):
      if X[i][0]+p==X[j][0] and X[i][1]+q==X[j][1]:
        r-=1
  return r

P=0
for i in range(N):
  for j in range(i+1,N):
    P=min(P,solve(X[j][0]-X[i][0],X[j][1]-X[i][1]))
print(N+P)