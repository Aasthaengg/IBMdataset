s=input()+"DDD"
n=len(s)-3
i=0
ac=0
c=0
while i<n:
  if s[i]=="A":
    ac+=1
    i+=1
  elif s[i:i+2]=="BC":
    c+=ac
    i+=2
  else:
    ac=0
    i+=1
print(c)