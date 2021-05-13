s=input()
t=''
i=0
while i<len(s):
  if s[i]=='A':
    t+='A'
    i+=1
  elif s[i]=='B':
    if i!=len(s)-1:
      if s[i+1]=='C':
        t+='B'
        i+=2
      else:
        t+='X'
        i+=1
    else:
      i+=1
  else:
    t+='X'
    i+=1
b=0
x=0
for i in range(len(t))[::-1]:
  if t[i]=='B':
    b+=1
  elif t[i]=='A':
    x+=b
  else:
    b=0
print(x)