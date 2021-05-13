N=int(input())
S=list()
for i in range(N):
  S.append(input())
M=int(input())
T=list()
for i in range(M):
  T.append(input())
ans=0
for i in S:
  v=S.count(i)-T.count(i)
  if v>ans:
    ans=v
print(ans)