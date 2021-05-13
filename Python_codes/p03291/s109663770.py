s=input()
mod=10**9+7
a,ab,abc=0,0,0
q=0
for c in s:
  if c=='A':
    a=(a+pow(3,q,mod))%mod
  elif c=='B':
    ab=(a+ab)%mod
  elif c=='C':
    abc=(ab+abc)%mod
  else:
    a,ab,abc=(3*a+pow(3,q,mod))%mod,(3*ab+a)%mod,(3*abc+ab)%mod
    q+=1
print(abc)