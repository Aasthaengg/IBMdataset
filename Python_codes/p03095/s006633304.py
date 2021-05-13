N=int(input())
S=input()
A={}
for i in S:
  if i not in A:
    A[i]=1
  else:
    A[i]+=1
ans=1
for i in A.values():
  ans*=(i+1)
  ans%=(10**9+7)
print(ans-1)