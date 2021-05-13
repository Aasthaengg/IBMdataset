s=input()
t=input()
lens=len(s)
lent=len(t)

alp="abcdefghijklmnopqrstuvwxyz"

D={c : {i:-1 for i in range(lens*2)} for c in alp}

tab={c:0 for c in alp}

for i in range(lens*2):
    nowc=s[i%lens]
    for q in range(tab[nowc],i+1):
        D[nowc][q]=i
    tab[nowc]=i+1

ans=0
pos=0
for i in range(lent):
    nowc=t[i]
    if D[nowc][pos]==-1:
        print(-1)
        break
    ans+=D[nowc][pos]-pos+1
    #print(ans)
    pos=D[nowc][pos]+1
    pos%=lens
else:
    print(ans)