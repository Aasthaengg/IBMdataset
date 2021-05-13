import itertools
N,K=map(int,input().split())
S=input()
gr=itertools.groupby(S)
li=[] if S[0]=='1' else [0]
for key,group in gr:
    li.append(len(list(group)))
res=0
cum=[0]*(len(li)+1)
for i in range(len(li)):
    cum[i+1]=cum[i]+li[i]
for i in range(0,len(li),2):
    r=i+2*K+1
    if r>=len(cum):
        r=len(cum)-1
    res=max(res,cum[r]-cum[i])
print(res)