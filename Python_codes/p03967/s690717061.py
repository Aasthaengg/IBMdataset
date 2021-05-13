s=input()

ans=0
g=0
for h in s:
    if g>0:
        #pを出せるなら出す
        g-=1
        if h=='g':
            ans+=1
    else:
        #pが出せないならg
        g+=1
        if h=='p':
            ans-=1

print(ans)