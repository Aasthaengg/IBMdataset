
N,A,B,C=map(int, input().split())

L=[]
for i in range(N):
    l=int(input())
    L.append(l)
L=sorted(L, reverse=True)

combs=[]
for b in range(4**N):
    nowlist=[[],[],[],[]]
    for i in range(N):
        mod=b%4
        nowlist[mod].append(L[i])
        b=b//4
    combs.append(nowlist)

#print(combs)

abc=[A,B,C]

ans=float("INF")
for c in combs:
    now=0
    for i in range(3):
        cn=c[i]
        n=abc[i]
        if len(cn)==0:
            break
        now+=(len(cn)-1)*10
        now+=abs(sum(cn)-n)
        if i==2:
            ans=min(ans, now)

print(ans)

