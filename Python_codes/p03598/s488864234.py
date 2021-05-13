N=int(input())
K=int(input())
l = list(map(int,input().split()))
ans=0
for i in range(N):
  n=K-l[i]
  nn=abs(n)
  if nn<l[i]:
    ans+=nn*2
  else:
    ans+=2*l[i]
print(ans)