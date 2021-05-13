s=list(input())
cnt=100
for i in range(26):
    x=chr(97+i)
    if x not in s:
        continue
    tmp=0
    dummy=s+[]
    while len(set(dummy))>1:
        tmp+=1
        newdum=[]
        for j in range(len(dummy)-1):
            if dummy[j]==x or dummy[j+1]==x:
                newdum.append(x)
            else:
                newdum.append(dummy[j])
        dummy=[]+newdum
    cnt=min(cnt,tmp)
print(cnt)
