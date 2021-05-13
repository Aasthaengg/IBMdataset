s=input()
ans=0
count=0
t=""
if s[0]=="A":
  ans+=1
for i in range(2,len(s)-1):
  # print(s[i])
  if s[i]=="C":
    count+=1
    t=s[1:i]+s[i+1:]	
# print(t)
if t.islower()==True and ans==1 and count==1:
  print("AC")
else:
  print("WA")