s=list(input())
s.append("D")
S=[]
i=0
while i<len(s):
  if s[i]=="A":
    S.append(1)
    i=i+1
  elif s[i]=="B":
    if s[i+1]=="C":
      S.append(2)
      i=i+2
    else:
      S.append(3)
      i=i+1
  else:
    S.append(3)
    i=i+1
ans=0
a=0
b=0
for i in range(len(S)):
  if S[i]==1:
    a=a+1
  elif S[i]==2:
    b=b+1
    ans=ans+a
  else:
    a=0
    b=0
print(ans)