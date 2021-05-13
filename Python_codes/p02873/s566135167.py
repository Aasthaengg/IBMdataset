s=input()
n=len(s)
if s[0]=="<":
    nari=0
    scnt,dcnt=0,1
else:
    nari=1
    scnt,dcnt=1,0
ans=0
sfla,dfla=0,0
for i in range(n):
    if nari==0:
        if s[i]=="<":
            scnt+=1
        elif s[i]==">":
            ans+=scnt*(scnt-1)//2
            sfla=scnt
            nari=1
            scnt=1
            dlas=0

    elif nari==1:
        if s[i]==">":
            dcnt+=1
        elif s[i]=="<":
            ans+=dcnt*(dcnt-1)//2
            dfla=dcnt
            nari=0
            dcnt=1
            dlas=1
            ans+=(max(dfla,sfla))
    # print(ans)
if dcnt!=1:
    ans+=dcnt*(dcnt+1)//2
elif scnt!=1:
    ans+=scnt*(scnt+1)//2
else: ans+=1
print(ans)
