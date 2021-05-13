S=list(input())
ans=103
for i in range(26):
  A=[-1]
  for j in range(len(S)):
    if S[j]==chr(i+97):
      A.append(j)
  A.append(j+1)
  a=0
  for j in range(len(A)-1):
    a=max(a,A[j+1]-A[j]-1)
  if a<ans:
    ans=a
print(ans)