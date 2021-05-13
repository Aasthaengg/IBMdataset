n = int(input())
ss=[list(map(str,input().split())) for i in range(n)]
zenhan=[]
kouhan=[]

for i in range(n):
    retu = list(ss[i])[0]
    acnt=0
    bcnt=0
    for j in range(len(retu)):
        if retu[j] == "(":
            acnt+=1
        elif acnt>0:
            acnt-=1
    a=acnt

    acnt=0
    bcnt=0
    for j in reversed(range(len(retu))):
        if retu[j] == ")":
            bcnt+=1
        elif bcnt>0:
            bcnt-=1
    b=bcnt

    if a!=0 or b!=0:
        if a < b:
            kouhan.append([a,b,retu])
        else:
            zenhan.append([a,b,retu])

zenhan.sort(key=lambda x:x[1])
kouhan.sort(reverse=True)
cnt=0
for tmp in zenhan:
    retu=tmp[2]
    for i in range(len(retu)):
        if retu[i] == "(":
            cnt+=1
        else:
            cnt-=1
        if cnt<0:
            print("No")
            exit()

for tmp in kouhan:
    retu=tmp[2]
    for i in range(len(retu)):
        if retu[i] == "(":
            cnt+=1
        else:
            cnt-=1
        if cnt<0:
            print("No")
            exit()
if cnt!=0:
    print("No")
else:
    print("Yes")
