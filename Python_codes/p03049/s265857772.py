N=int(input())
s=[input() for _ in range(N)]

s1,s2,s3,s4=[],[],[],[]
ans=0
for i in range(N):
  ans += s[i].count('AB')
  if s[i][0]=='B' and s[i][-1]=='A':
    s1.append(s[i])
  elif s[i][-1]=='A':
    s2.append(s[i])
  elif s[i][0]=='B':
    s3.append(s[i])
  else:
    s4.append(s[i])
    
if len(s2) and len(s3):
  ans += len(s1)+1
  ans += min(len(s2)-1,len(s3)-1)
  
elif len(s1) and len(s2):
  ans += len(s1)
  
elif len(s1) and len(s3):
  ans += len(s1)
  
elif len(s1):
  ans += len(s1)-1

print(ans)