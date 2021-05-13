s=input()
ans=[0]*(len(s)+1)
i=1
now="R"
cnt=1
col=[]
while i<len(s):
    if s[i]==now:
        cnt+=1
    else:
        col.append(cnt)
        if now=="R":now="L"
        else:now="R"
        cnt=1
    i+=1
col.append(cnt)
import math
k=0
for i in range(0,len(col),2):
    ans[k+col[i]]=math.ceil(col[i]/2)+math.floor(col[i+1]/2)
    ans[k+col[i]+1]=math.ceil(col[i+1]/2)+math.floor(col[i]/2)
    k+=col[i]+col[i+1]

ans.pop(0)
print(*ans)