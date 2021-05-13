N=int(input())
C=list(map(int,input().split()))
ans=[0]*(N+1)
for i in range(N):
  ans[C[i]]=i+1
ans.remove(0)
ans=' '.join([str(n) for n in ans])
print(ans)