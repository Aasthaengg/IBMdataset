s=input()
str=["A","K","I","H","A","B","A","R","A"]
count=0
ans=0
for i in range(9):
    if count==len(s) and i<8:
        ans=1
        break
    elif count==len(s):
        break
    if s[count]==str[i]:
        count+=1
    elif s[count]!=str[i] and str[i]!="A":
        ans=1
        break
if len(s)>9:
    ans=1
if ans==1:
    print("NO")
else:
    print("YES")
