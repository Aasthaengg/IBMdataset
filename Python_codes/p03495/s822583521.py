from collections import defaultdict

N,K=map(int,input().split())
A=list(map(int,input().split()))

d={}
for i in range(N):
    if A[i] in d.keys():
        d[A[i]]+=1
    else:
        d[A[i]]=1

dic=sorted(d.items(), key=lambda x:x[1])
if len(dic)<=K:
    print(0)
else:
    ans=0
    cnt=len(dic)
    for key,value in dic:
        if cnt-1==K:
            ans+=value
            print(ans)
            break
        else:
            ans+=value
            cnt-=1