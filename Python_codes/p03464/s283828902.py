N=int(input())
A=list(map(int, input().split()))
x=2
y=2
A=A[::-1]
for i in range(N):
  if y<A[i]:
    print(-1)
    exit()
  else:
    if x<A[i]:
      x=A[i]
    if x%A[i]!=0:
      x+=A[i]-x%A[i]
    if y%A[i]!=0:
      y-=y%A[i]
    y+=A[i]-1
    if x>y:
      print(-1)
      exit()
print(x,y)