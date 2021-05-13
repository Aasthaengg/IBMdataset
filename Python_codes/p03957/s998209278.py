s=input()
n=len(s)
c=0
for i in range(n):
  if c==1 and s[i]=="F":
    print("Yes")
    exit()
  if c==0 and s[i]=="C":
    c+=1
print("No")