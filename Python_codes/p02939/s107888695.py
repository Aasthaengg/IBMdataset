s=input()
i=1
s0=s[0]
ct=1
while i<len(s)-1:
  if s0==s[i]:
    s0=s[i:i+2]
    i+=2
  else:
    s0=s[i]
    i+=1
  ct+=1
if i>=len(s):
  print(ct)
elif s0==s[i]:
  print(ct)
else:
  print(ct+1)