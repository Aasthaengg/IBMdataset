N=int(input())
s=str(input())
r=[]
b=[]
for i in range(N):

  if s[i]=='R':
    r.append(s[i])
  else:
    b.append(s[i])
if len(r) > len(b):
  print('Yes')
else:
  print('No')
