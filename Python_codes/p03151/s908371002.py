n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
f=0
mi=0
pr=[]
for i in range(n):
  if a[i]-b[i]<0:
    mi+=(b[i]-a[i])
    f+=1
  else:
    pr.append(a[i]-b[i])
if f==0:
  print(0)
  exit()
if sum(pr)<mi:
  print(-1)
  exit()
pr.sort(reverse=True)
p=0
for i in range(len(pr)):
  p+=pr[i]
  f+=1
  if p>=mi:
    break
print(f)