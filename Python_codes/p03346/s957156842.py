from itertools import groupby

N=int(input())
P=[]
for i in range(0,N):
    P.append(int(input()))

dic={i:0 for i in range(1,N+1)}
data=['No' for i in range(0,N)]
for i in range(0,N):
    test=P[i]
    if test!=N:
        if dic[test+1]==0:
            data[test-1]='Yes'
    dic[test]+=1

data=groupby(data)
ans=0
for key,group in data:
    g=len(list(group))
    if key=='Yes':
        ans=max(ans,g)

print(N-ans-1)