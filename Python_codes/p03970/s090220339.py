s=str(input())

def solve(s):
  res=0
  t="CODEFESTIVAL2016"
  for i in range(len(s)):
    if s[i]!=t[i]:
      res+=1
  return res
  
print(solve(s))