s=input()
n=len(s)
def isk(S):
  l=len(S)
  f=1
  for i in range(l//2+1):
    if S[i]==S[l-i-1]:
      f*=1
    else:
      f=0
  if f:
    return True
  else:
    return False
  
if isk(s) and isk(s[:(n-1)//2]) and isk(s[(n+1)//2:]):
  print('Yes')
else:
  print('No')