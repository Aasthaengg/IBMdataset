N=int(input())
a=[]
m=1
for i in range(N):
  t=int(input())
  a.append(t)
for j in range(N):
  m=a[m-1]
  if m==2:
    print(j+1)
    break
else:
  print(-1)