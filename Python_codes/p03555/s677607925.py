S1=input()
S2=input()
ans=1
for i in range(3):
  if S1[i]!=S2[2-i]:
    ans=ans*0
print(["NO","YES"][ans])
