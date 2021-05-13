s=input()
maxc=c=0
for i in range(len(s)):
    if s[i]=="A" or s[i]=="C" or s[i]=="G" or s[i]=="T" :
        c+=1
        maxc=max(c,maxc)
    else:
        c=0
print(maxc)

