from collections import Counter
s=input()
ch=set([c for c in s])
ans=101

for c in ch:
    cur=s
    cnt=0
    while len(set([x for x in cur]))>1:
        cnt+=1
        tmp=''
        for i in range(len(cur)-1):
            if cur[i]==c or cur[i+1]==c:
                tmp+=c
            else:
                tmp+=cur[i]
        cur=tmp
    ans=min(ans,cnt)

print(ans)