N,C,K=map(int,input().split())
T=[int(input()) for i in range(N)]
T.sort()
res=0#乗客
time=0#発車K分前
ans=0

for i in range(len(T)):
    if res!=0 and time+K<T[i]:
        ans+=1
        res=1
        time=T[i]

    else:
        res+=1
        if res==1:
            time=T[i]
        if res==C:
            ans+=1
            res=0

if res>0:
    ans+=1

print(ans)
