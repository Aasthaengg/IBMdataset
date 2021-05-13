s=input()
ans=0
res=0
w=0
l=0
for i in range(len(s)):
    if res==0:
        res+=1
        if s[i]=='p':
            l+=1
    else:
        if s[i]=='p':
            res-=1
        else:
            res-=1
            w+=1
print(w-l)