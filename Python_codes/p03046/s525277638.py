m,k=map(int,input().split())
if m==0 and k==0:
  print(0,0)
elif m==1 and k==1:
  print(-1)
elif k>2**m-1:
  print(-1)
elif k==2**m-1:
  Ans=[]
  for i in range(2**m-1):
    Ans.append(2**m-2-i)
  Ans.append(2**m-1)
  for i in range(2**m):
    Ans.append(i)
  print(*Ans)
else:
  if k==0:
    Ans=[]
    for i in range(2**m):
      Ans.append(i)
      Ans.append(i)
    print(*Ans)
  else:
    Ans=[k]
    for i in range(2**m):
      if i!=k:
        Ans.append(i)
    Ans.append(k)
    for i in range(2**m):
      if i!=2**m-1-k:
        Ans.append(2**m-1-i)
    print(*Ans)