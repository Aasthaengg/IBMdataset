s=list(input())
s1=[]
for i in range(len(s)):
  if s[i]!="x":
    s1.append(s[i])
s2=s1[::-1]
if s1!=s2:
  print(-1)
  exit()
if s1==[]:
  print(0)
  exit()
A1=[0]*10**5
A2=[0]*10**5
i=0
j=0
while i<=len(s1)//2:
  if s[j]=="x":
    A1[i]+=1
    j=j+1
  else:
    i=i+1
    j=j+1
i=0
j=0
while i<=len(s1)//2:
  if s[-1-j]=="x":
    A2[i]+=1
    j=j+1
  else:
    i=i+1
    j=j+1
ans=0
for i in range(10**5):
  ans=ans+abs(A1[i]-A2[i])
print(ans)