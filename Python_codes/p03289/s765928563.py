S=input()
MojiNagasa=len(S)
flag=True
if S[0]!="A":
  flag=False
count=0
for i in range(1,MojiNagasa):
  if S[i].isupper():
    if i==1 or i==MojiNagasa-1 or S[i]!='C':
      flag=False
    count+=1
if (count!=1):
  flag=False
print("AC" if flag else "WA")
