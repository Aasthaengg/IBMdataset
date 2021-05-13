N,K=map(int,input().split())
l=list()
for i in range(N):
  l.append(int(input()))
l.sort()
ans=int(l[K-1])-int(l[0])
for i in range(1,N-K+1):
  key=int(l[i+K-1])-int(l[i])
  if ans>key:
    ans=key
print(ans)