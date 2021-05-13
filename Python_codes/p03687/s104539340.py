from copy import deepcopy
ss=list(input())
ans=float("inf")
n=len(ss)
for i in range(n):
    s=deepcopy(ss)
    t=ss[i]
    flg=True
    while flg:
        tmp=""
        if all(s[k]==t for k in range(len(s))):
            tt=len(ss)-len(s)
            if tt<ans:
                ans=tt
            flg=False
            break
        for j in range(len(s)-1):
            
            if s[j]==t or s[j+1]==t:
                tmp+=t
            else:
                tmp+=s[j]
        s=tmp
print(ans)