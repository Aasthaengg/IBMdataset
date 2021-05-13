A=list(input())
B=list(input())
ans=0
for i in range(len(A)):
   if A[i] != B[i]:
      ans+=1
print(ans)