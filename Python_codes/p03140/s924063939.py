N=int(input())
A,B,C=input(),input(),input(),

ans=0
for i in range(N):
  if A[i]==B[i]==C[i]:
    ans+=0
  elif A[i]!=B[i] and A[i]!=C[i] and B[i]!=C[i]:
    ans+=2
  else:
    ans+=1
  #print(i,ans)
print(ans)