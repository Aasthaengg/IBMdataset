s=input()

tmp=""
bk=""
cnt=0

for ss in s:
    tmp+=ss
    if bk != tmp:
        cnt+=1
        bk=tmp
        tmp=""

    
print(cnt)
        
