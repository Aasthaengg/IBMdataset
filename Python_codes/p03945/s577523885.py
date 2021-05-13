s=list(input())
l=len(s)

for i in range(l-1):
  if s[i]==s[i+1]:
    s[i]='0'
    
print(s.count('B')+s.count('W')-1)