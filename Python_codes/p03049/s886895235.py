n=int(input())
s=[None]*n
nA=0
nB=0
nAB=0
ans=0
for i in range(n):
    ss = input()
    ans+= ss.count("AB")
    if ss[0]=="B" and ss[-1]=="A":
        nAB+=1
    elif ss[0]=="B":
        nB+=1
    elif ss[-1]=="A":
        nA+=1
    s[i]=ss

if nAB==0:
    ans+=min(nA,nB)
elif nA==0 and nB==0:
    ans+=nAB-1
elif nA==0:
    ans+=nAB
elif nB==0:
    ans+=nAB
else:
    ans+=nAB+1 + min(nA,nB)-1
print(ans)