s=input()
x=0
y=0
j=0
for i in range(len(s)):
  if j==0 and s[i]=="A":
    j+=1
    x=i
  elif j==1 and s[i]=="Z":
    y=i
print(y-x+1)
