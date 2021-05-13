#import re
x=input()
ans=0
ns=0
nt=0
for i in range(len(x)):
  if x[i]=='S':
    ns+=1
  elif ns>0 and x[i]=='T':
    ns-=1
  else:
    ans+=1
print(ans+ns)
