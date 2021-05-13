N,M=map(int,input().split())
acs=[0 for i in range(N)]
wa=[0 for i in range(N)]

for  i in range(M):
    p,S=map(str,input().split())
    p=int(p)
    if S=='AC':
        acs[p-1]=1
    elif S=='WA' and acs[p-1]==0: 
        wa[p-1]+=1
for i in range(N):
    if acs[i]==0:
        wa[i]=0
ans=[sum(acs),sum(wa)]
print(*ans)