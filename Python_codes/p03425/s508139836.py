n=int(input())
s=[input() for i in range(n)]

cnt=[0]*5

for i in range(n):
    if s[i][0]=='M':cnt[0]+=1
    elif s[i][0]=='A':cnt[1]+=1
    elif s[i][0]=='R':cnt[2]+=1
    elif s[i][0]=='C':cnt[3]+=1
    elif s[i][0]=='H':cnt[4]+=1
    else:pass

ans=0
keta=[0]*5
for i in range(7,29):
 
    for x in range(5):
        keta[x]=(i>>x)&1

    if sum(keta)!=3:
        continue
    
    product=1
    for j in range(5):
        if keta[j]==1:
            product*=cnt[j]

    ans+=product

print(ans)