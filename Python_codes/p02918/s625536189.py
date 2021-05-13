import itertools

N,K=map(int,input().split())
S=input()

ans=0
for _,l in itertools.groupby(S):
  ans+=len(list(l))-1
ans+=2*K
ans=min(ans,N-1)
print(ans)