s=input()
c=0
a=0
for i in range(len(s)):
 if s[i]=="W":a+=i-c;c+=1
print(a)