s=input()

bb='CODEFESTIVAL2016'

ans=0
i=0
while i<len(bb):
    
    if s[i]!=bb[i]:
        ans+=1

    i+=1

print(ans)