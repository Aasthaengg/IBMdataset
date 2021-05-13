count=0
s=input()
temp = s[0]
for i in range(1,len(s)):
    if s[i]!=temp:
        count+=1
    temp=s[i]

if count==0 : print(0)
else : print(count)