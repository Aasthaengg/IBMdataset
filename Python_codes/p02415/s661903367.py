s=str(input())
m=''
for i in range(len(s)):
    c=str(s[i])
    if(s[i].islower()):
        c=s[i].upper()
    elif(s[i].isupper()):
        c=s[i].lower()
    else:
         c=s[i]
    m+=c
print(m)
        
