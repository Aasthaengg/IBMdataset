N=int(input())
a=list(map(int, input().split()))
S=1
c=0
for j in range(N):
  if S==a[j]:
    S+=1
  elif S!=a[j]:
    c+=1
if c==N:
  print(-1)
  exit()
print(c)