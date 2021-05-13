S=input()
K=int(input())
ans=0
for i in range(len(S)):
  a=int(S[i])
  if a==1:
    ans+=1
  else:
    print(a)
    break
  if ans>=K:
    print(a)
    break