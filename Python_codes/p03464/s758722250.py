N=int(input())
A=list(map(int, input().split()))
x=2
y=2
A=A[::-1]
for i in range(N):
  nmin=((x+A[i]-1)//A[i])*A[i]
  nmax=y-y%A[i]
  if nmin>nmax:
    print(-1)
    exit()
  x=nmin
  y=nmax+A[i]-1
print(x,y)