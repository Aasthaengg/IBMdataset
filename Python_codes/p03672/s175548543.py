s=list(input())
while len(s)!=0:
  s.pop(len(s)-1)
  if s[:len(s)//2]*2==s:
    break
print(len(s))