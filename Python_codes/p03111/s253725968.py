N,A,B,C=map(int,input().split())
L=[int(input()) for i in range(N)]
def f(X):
  global N,A,B,C,L
  if len(X)==N:
    a,b,c=0,0,0
    for i in range(N):
      a+=X[i][0]
      b+=X[i][1]
      c+=X[i][2]
    if min(a,b,c)==0:
      return 10**16
    else:
      return abs(A-a)+abs(B-b)+abs(C-c)
  return min(f(X+[[0,0,0]]),f(X+[[L[len(X)],0,0]])+10,f(X+[[0,L[len(X)],0]])+10,f(X+[[0,0,L[len(X)]]])+10)

print(f([])-30)