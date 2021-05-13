N,K=map(int,input().split())
p=list(map(int,input().split()))
best=0
for i in range(K):
  best+=(p[i]+1)/2
#print(best)
temp=best
for i in range(N-K):
  temp+=(p[K+i]+1)/2
  temp-=(p[i]+1)/2
  best=max(best,temp)
print(best)