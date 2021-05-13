N=int(input())
M,K=map(int,input().split())
ans=K
for i in range(N):
  s=int(input())
  ans+=1+(M-1)//s
print(ans)