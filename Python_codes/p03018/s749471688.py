ans=0
for x in input().replace('BC','y').replace('A','x').replace('B',' ').replace('C',' ').split():
    c=0
    for t in x:
        if t=='y':
            ans+=c
        else:c+=1
print(ans)