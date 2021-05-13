s=input()
flag=True
for i in range(len(s)-1):
    for j in range(i+1,len(s)):
        if s[i]==s[j]:
            flag=False
            break
    if not(flag):
        break
print("yes") if flag else print("no")