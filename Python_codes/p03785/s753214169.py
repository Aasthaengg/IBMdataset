N,C,K=map(int, input().split())
T=[]
for i in range(N):
    t=int(input())
    T.append(t)

T=sorted(T)
ans=0
mint=T[0]
now=1
for i in range(1,N):
    t=T[i]
    if now==C:
        ans+=1
        now=1
        mint=t
    elif t-mint<=K:
        now+=1
    else:
        ans+=1
        now=1
        mint=t
    if i==N-1:
        ans+=1
print(ans)