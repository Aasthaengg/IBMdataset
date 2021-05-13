s=input()

s=s.replace("BC","D")

count=0

c=0
while c<len(s):
    if s[c]=="A" or s[c]=="D":
        d=c
        while s[d]=="A" or s[d]=="D":
            d+=1
            if d==len(s):
                break
        an=0
        for i in range(c,d):
            if s[i]=="A":
                an+=1
            else:
                count+=an
        c=d
    else:
        c+=1

print(count)