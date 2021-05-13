import copy
N=int(input())
ans=[]
S=[int(input()) for i in range(N)]
W=copy.copy(S)
W.sort()
for i in range(N):
  if W[-1]==S[i]:
    ans.append(W[-2])
  else:
    ans.append(W[-1])
for j in range(N):
  print(ans[j])