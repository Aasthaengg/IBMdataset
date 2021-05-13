S=input()
K=int(input())
tmp=100
for i in range(len(S)):
  if S[i]!='1':
    tmp=i
    break
if K<=tmp:
  ans=S[0]
else:
  ans=S[tmp]
print(ans)