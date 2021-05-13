N,M=map(int,input().split())
s=[list(map(int,input().split()))[1:] for i in range(M)]
p=list(map(int,input().split()))
ans,cnt=0,0
for n in range(2**N):
  for m in range(M):
    cnt=0
    for i in range(N):
      if (n>>i)&1 and i+1 in s[m]:
        cnt+=1
    if cnt%2!=p[m]:
      break
  else:
    ans+=1
print(ans)