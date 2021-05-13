S=input()
T=input()
n=len(S)
s,t=[],[]
for i in range(n):
  s.append(S[i])
  t.append(T[i])
for i in range(n):
  p=s[0]
  for j in range(1,n):
    s[j-1]=s[j]
  s[n-1]=p
  if s==t:
    print('Yes')
    exit()
print('No')