S = input()

def iskai(s):
  result=False
  if s == s[::-1]:
    result=True
  return(result)

ans = 'No'
hf = len(S)//2 + 1

if iskai(S) and iskai(S[:hf-1]) and iskai(S[hf:]):
  ans = 'Yes'
  
print(ans)