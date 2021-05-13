N,K=map(int,input().split())
P=list(map(lambda x:int(x)-1,input().split()))
C=list(map(int,input().split()))

if K<=N:
  ans = -10**9
  for i in range(N):
    now,last = i,0
    for _ in range(K):
      last += C[P[now]]
      ans = max(ans,last)
      now=P[now]
  print(ans)
  exit()
ans = -10**9
for i in range(N):
  tmp,now,done = [0],i,set()
  for _ in range(N+1):
  #while now not in done:
    tmp.append(tmp[-1]+C[P[now]])
    if P[now] == i:
      break
    now = P[now]
  tmp = tmp[1:]
  cnt = len(tmp)
  m = max(tmp)
  ans = max(ans,m,tmp[-1]*(K//cnt-1)+m)
  if K%cnt != 0:
    ans = max(ans, tmp[-1]*(K//cnt)+max(tmp[:K%cnt]))
    #print(i,ans,tmp)
print(ans)


