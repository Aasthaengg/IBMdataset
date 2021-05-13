s=input()
rcnt,lcnt=0,0
jidai=0
rsatan=0
ans=[0 for _ in range(len(s))]
for i in range(len(s)):
    if jidai==0:
        if s[i]=="R":
            rcnt+=1
        elif s[i]=="L":
            rrem=i-1
            lrem=i
            lcnt+=1
            jidai=1
    elif jidai==1:
        if s[i]=="L":
            lcnt+=1
        elif s[i]=="R":
            jidai=0
            if (lcnt+rcnt)%2==0:
                ans[rrem],ans[lrem]=(lcnt+rcnt)//2,(lcnt+rcnt)//2
            else:
                if (rrem-rsatan)%2==0:
                    ans[rrem],ans[lrem]=(lcnt+rcnt)//2+1,(lcnt+rcnt)//2
                else:
                    ans[rrem],ans[lrem]=(lcnt+rcnt)//2,1+(lcnt+rcnt)//2

            rcnt,lcnt=1,0
            rsatan=i

if (lcnt+rcnt)%2==0:
    ans[rrem],ans[lrem]=(lcnt+rcnt)//2,(lcnt+rcnt)//2
else:
    if (rrem-rsatan)%2==0:
        ans[rrem],ans[lrem]=(lcnt+rcnt)//2+1,(lcnt+rcnt)//2
    else:
        ans[rrem],ans[lrem]=(lcnt+rcnt)//2,1+(lcnt+rcnt)//2

print(' '.join(map(str, ans)))