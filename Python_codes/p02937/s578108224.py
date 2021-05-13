from bisect import bisect_left
s=input()
t=input()
al=[[] for i in range(26)]
for i in range(len(s)):
    al[ord(s[i])-97].append(i)
ans=0
now=-1
ok=True
for i in range(len(t)):
    c=t[i]
    o=ord(c)-97
    b=bisect_left(al[o],now+1)
    if(b==len(al[o])):
        ans+=len(s)-now-1
        now=-1
        b=bisect_left(al[o],now)
        if(b==len(al[o])):
            ok=False
    if ok:
        ans+=al[o][b]-now
        now=al[o][b]
    else:
        print(-1)
        exit()
print(ans)