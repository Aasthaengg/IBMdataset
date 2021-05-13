N=int(input())
S=input()
ans,r,g,b=0,0,0,0
for s in S:
  if s=='R':
    r+=1
  elif s=='G':
    g+=1
  elif s=='B':
    b+=1
ans=r*g*b
for i in range(N-2):
  a=S[i]
  for j in range(i+1,N-1):
    if 2*j-i>=N:
      break
    b,c=S[j],S[j+j-i]
    if a!=b and b!=c and c!=a:
      ans-=1
print(ans)