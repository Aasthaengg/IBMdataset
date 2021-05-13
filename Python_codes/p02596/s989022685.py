K=int(input())

x=7%K
i=1
flag=0
for j in range(K+1):
  if x==0:
    print(i)
    flag=1
    break
  x=(10*x+7)%K
  i+=1


if flag==0:
  print(-1)