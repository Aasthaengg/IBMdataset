N=int(input())
*a,=map(int,input().split())

if N == 1:
  print(0)
  exit()

m = sum(a)

MIN=10**20
argmin=-1
for i in range(N):
  if MIN>abs(m-a[i]*N):
    MIN = abs(m-a[i]*N)
    argmin = i
print(argmin)