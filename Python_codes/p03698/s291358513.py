from collections import Counter

s=input()

n=len(Counter(s))

if n==len(s):
  ans="yes"
else:
  ans="no"
  
print(ans)