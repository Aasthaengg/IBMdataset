s=list(input())
count=0
i=0
j=len(s)-1
while j-i>=1:
    if s[i]==s[j]:
        i+=1
        j-=1
    elif s[i]=='x':
        count+=1
        i+=1
    elif s[j]=='x':
        count+=1
        j-=1
    else:
        print(-1)
        exit()
print(count)
    

