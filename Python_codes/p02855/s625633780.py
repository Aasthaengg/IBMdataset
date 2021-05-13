H,W,K=map(int,input().split())
S=[input()for _ in range(H)]
ans=[['0']*W for _ in range(H)]

i=U=L=0
now=0
now2=0
while i<H:
    j=0
    ok=0
    while j<W:
        if S[i][j]=='#':
            ok+=1
            now+=1
        if ok:
            ans[i][j]=now
        if ok==1:
            for k in range(j):
                ans[i][k]=now
        j+=1
    if ok>0 and now2==0:
        now2=ans[i]
    i+=1

i=0
while i<H:
    if '0' in ans[i]:
        ans[i]=now2
    else:
        now2=ans[i]
    i+=1

for a in ans:
    print(*a)