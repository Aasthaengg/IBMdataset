string=list(input())
n=len(string)
s=set()
ans=10**4

for target in string:
    if target in s:
        continue
    
    cnt=0
    tmp_max=0
    for i in string:
        if i!=target:
            cnt+=1
        else:
            tmp_max=max(tmp_max,cnt)
            cnt=0
    tmp_max=max(tmp_max,cnt)
    ans=min(ans,tmp_max)
        
print(ans)