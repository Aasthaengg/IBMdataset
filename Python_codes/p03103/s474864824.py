N,M=map(int,input().split())
C=[]
ans=0
cnt=0
for i in range(N):
  a,b=map(int,input().split())
  C.append((a,b))
C=sorted(C)
for i in range(N):
  if cnt+C[i][1]<=M:
    cnt+=C[i][1]
    ans+=C[i][1]*C[i][0]
  else:
    break
print((M-cnt)*C[i][0]+ans)