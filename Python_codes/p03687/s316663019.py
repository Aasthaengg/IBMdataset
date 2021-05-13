s=input()
s2=[]
for i in range(len(s)):
    s2.append(s[i])
s3=sorted(list(set(s2)))
ans=10**9
for x in range(len(s3)):
    memo=s3[x]
    cnt=0
    t=s
    p=len(s.replace(memo,""))
    while p!=0:
        t2=""
        l=len(t)
        k=0
        while k<l-1:
            if t[k]==memo or t[k+1]==memo:
                t2=t2+memo
            else:
                t2=t2+t[k]
            k+=1
        t=t2
        cnt+=1
        p=len(t2.replace(memo,""))
    if cnt<ans:
        ans=cnt
print(ans)
