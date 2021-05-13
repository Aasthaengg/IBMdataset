s=input()
n=0
c=0
i=0
while i<len(s):
  if s[i]=="A":
    c+=1
  elif s[i:i+2]=="BC":
    n+=c
    i+=1
  else:
    c=0
  i+=1
print(n)
