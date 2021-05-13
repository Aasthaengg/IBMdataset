s=input()
c=0
for i in range(1,len(s)):
    if s[-i]==s[-i-1]:
        continue
    else:
        c+=1
print(c)