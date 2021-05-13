f=1
a=0
b=0
c=0

for i in range(int(input())):
  s=input()
  if s[0]=="B":
    b+=1
  if s[-1]=="A":
    a+=1
  if (not(s[0]=="B" and s[-1]=="A"))and(s[0]=="B" or s[-1]=="A"):
    f=0
  for j in range(len(s)-1):
    if s[j:j+2]=="AB":
      c+=1
if min(a,b)==0:
  f=0
print(min(a,b)+c-f)
