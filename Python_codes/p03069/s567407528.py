n=int(input())
S=list(input())
W=[0]*(n+1)
B=[0]*(n+1)
for i in range(n):
  if S[i]=="#":
    B[i+1]=B[i]+1
  else:
    B[i+1]=B[i]
for i in range(n-1,-1,-1):
  if S[i]==".":
    W[i]=W[i+1]+1
  else:
    W[i]=W[i+1]
ans=10**10
for i in range(n+1):
  a=W[i]+B[i]
  if a<ans:
    ans=a
print(ans)