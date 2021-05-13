N,Q=map(int,input().split())
S=input()

s=[0]*(N+1)
for i in range(N):
  if i+1<N and S[i]=="A" and S[i+1]=="C":
    s[i+1]=s[i]+1
  else:
    s[i+1]=s[i]

for q in range(Q):
  l,r=map(int,input().split())
  print(s[r-1]-s[l-1])
