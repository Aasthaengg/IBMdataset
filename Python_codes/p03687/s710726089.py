from collections import Counter
s=input()
c=Counter(s).most_common()
ans=10**10
top=c[0][1]
for k,x in c:
    N=len(s)
    m=k
    cnt=0
    tmp=s
    for i in range(100):
        cn=Counter(tmp).most_common()
        if(cn[0][1]==len(tmp)):
            ans=min(ans,cnt)
            break
        l=''
        for j in range(N-1):
            if(tmp[j]==m or tmp[j+1]==m):
                l+=m
            else:
                l+=s[j]
        tmp=l
        cnt+=1
        N-=1
print(ans)