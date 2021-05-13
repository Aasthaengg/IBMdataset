N,K=map(int,input().split())
H=sorted(list(map(int,input().split())),reverse=True)
H=H[K:]
ans=0
if K<N:
  for x in H:
    ans+=x
print(ans)
