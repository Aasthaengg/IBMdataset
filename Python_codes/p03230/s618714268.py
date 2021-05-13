n=int(input())
k=0
for i in range(1,n+1):
  if (i*(i+1))//2==n:
    k=i
    break
else:
  k=-1
if k==-1:
  print('No')
else:
  arr=[[k] for _ in range(k+1)]
  tmp=0
  tk=0
  while k-tk>0:
    for i in range(tmp+1,tmp+k+1-tk):
      arr[tk].append(i)
    for i in range(tk+1,k+1):
      arr[i].append(tmp+i-tk)
    tmp+=(k-tk)
    tk+=1
  print('Yes')
  print(k+1)
  for row in arr:
    print(*row)