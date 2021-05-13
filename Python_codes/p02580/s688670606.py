H,W,M=map(int,input().split())
s=[list(map(int,input().split())) for _ in range(M)]
Tr=[0 for _ in range(H+1)]
Tc=[0 for _ in range(W+1)]
for i in range(M):
    Tr[s[i][0]]+=1
    Tc[s[i][1]]+=1
mr=max(Tr)
mc=max(Tc)
Mr=[0 for _ in range(H+1)]
Mc=[0 for _ in range(W+1)]
Nmr=0
Nmc=0
for i in range(len(Tr)):
    if Tr[i]==mr:
        Mr[i]=1
        Nmr+=1
for i in range(len(Tc)):
    if Tc[i]==mc:
        Mc[i]=1
        Nmc+=1
cnt=0
for i in range(M):
    if Mr[s[i][0]]==1 and Mc[s[i][1]]==1:
        cnt+=1
if cnt<Nmr*Nmc:
    print(mr+mc)
else:
    print(mr+mc-1)