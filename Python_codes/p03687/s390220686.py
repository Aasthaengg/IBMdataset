s=input()
A=list(set(s))
ans=100
for i in A:
  B=s+i
  C=[]
  pre=-1
  for j in range(len(s)+1):
    if B[j]==i:
      C.append(j-pre-1)
      pre=j
  ans=min(ans,max(C))
print(ans)