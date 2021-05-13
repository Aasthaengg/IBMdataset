N,X=list(map(int, input().split()))
L=list(map(int, input().split()))
c=1
x=0
for i in range(N):
  x+=L[i]
  if x<=X:
    c+=1
print(c)
