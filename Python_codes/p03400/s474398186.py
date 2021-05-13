N=int(input())
D, X=map(int, input().split())

def chococount(a,d):
  c=d//a
  if d%a!=0:
    c+=1
  return c
  
choco=X
for i in range(N):
  A=int(input())
  choco+=chococount(A,D)

print(choco)