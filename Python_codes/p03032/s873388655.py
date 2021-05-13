N,K=map(int,input().split())
V=list(map(int,input().split()))
if N<=K:
  W=sorted(V)
  h=sum(V)
  for i in range(K-N):
    if W[i]<0:
      h-=W[i]
    else:
      break
else:
  ans=[]
  for i in range(1,K+1):
    for j in range(i+1):
      l=V[0:i-j]+V[N-j:N]
      l.sort()
      H=sum(l)
      for k in range(min(i,K-i)):
        if l[k]<0:
          H-=l[k]
        else:
          break
      ans.append(H)
  h=max(ans)
print(h)