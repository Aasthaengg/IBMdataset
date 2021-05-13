n=int(input())
c=0
a=0
b=0
ab=0

for i in range(n):
  s=input()
  c+=s.count("AB")
  if s[0]=="B" and s[-1]=="A":ab+=1
  elif s[0]=="B":b+=1
  elif s[-1]=="A":a+=1

c+=min(a,b)+ab if max(a,b)!=0 else ab-1 if ab>0 else 0
print(c)