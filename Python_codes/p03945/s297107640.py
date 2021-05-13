s=input()
total=0
rec=s[0]
for i in range(1,len(s)):
    if rec!=s[i]:
        rec=s[i]
        total+=1
print(total)