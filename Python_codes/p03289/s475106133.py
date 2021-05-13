S=input()
p='AC'
o=0
u=0
for i in range(len(S)):
  if i==0 and S[i]!='A':
    p='WA'
    break
  if 2<=i<=len(S)-2:
    if S[i]=='C':
      o+=1
  if len(S)-2<i and o!=1:
    p='WA'
    break
  if ord(S[i])<97:
    if i==0 or 2<=i<=len(S)-2:
      continue
    else:
      p='WA'
      break
print(p)