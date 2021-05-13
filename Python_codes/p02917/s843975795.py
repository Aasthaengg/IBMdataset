N=int(input())
S=list(map(int,input().split()))
ans=0
ans+=S[0]
for i in range(N-2):
  ans+=min(S[i],S[i+1])
ans+=S[-1]
print(ans)