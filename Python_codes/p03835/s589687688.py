K,s=map(int,input().split())
cnt=0
for i in range(K+1):
  if s-i>2*K:
    continue
  for j in range(K+1):
    if s-i-j<0:
      break
    if s-i-j<=K:
      cnt+=1
print(cnt)