N,K=map(int,input().split())
fil=int((N-1)*(N-2)/2)
if K>fil:
  print(-1)
else:
  M=N-1+fil-K
  print(M)
  for i in range(N-1):
    print(1,i+2)
    count=0
  list=[]

  for j in range(2,N):
    for k in range(j+1,N+1):
      list.append((j,k))
  for i in range(fil-K):
    print(list[i][0],list[i][1])