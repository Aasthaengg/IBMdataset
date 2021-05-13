N,K=map(int,input().split())
if (N-1)*(N-2)//2<K:
  print(-1)
else:
  a=((N-2)*(N-1)//2)-K
  M=N-1+a
  print(M)
  for i in range(2,N+1):
    print(1,i)
  cnt=0
  for i in range(2,N):
    for j in range(i+1,N+1):
      if cnt<a:
        print(i,j)
        cnt+=1
      else:
        exit()