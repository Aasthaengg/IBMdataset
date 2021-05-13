k,s=map(int, input().split())
cnt=0
for p in range(k+1):
  for q in range(k+1):
    r=s-p-q
    if 0<=r<=k:
      cnt+=1
print(cnt)