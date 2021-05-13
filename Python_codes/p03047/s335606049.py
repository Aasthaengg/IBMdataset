N,K=map(int,input().split())
cnt=0

for i in range(1,N+1):
  if i+K-1<=N:
    cnt+=1

print(cnt)