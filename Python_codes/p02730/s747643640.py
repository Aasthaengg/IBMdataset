s = input()
n = len(s)
s1 = s[:(n-1)//2]
s2 = s[((n+3)//2)-1:]

def kaibun(S):
  for i,j in zip(S,S[::-1]):
    if i!=j:
      return False
  return True

if kaibun(s) and kaibun(s1) and kaibun(s2):
  print('Yes')
else:
  print('No')