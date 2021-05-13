N=int(input())
P=[]
for i in range(N):
    p=int(input())
    P.append(p)
Q=[0]*N
for i in range(N):
    Q[P[i]-1]=i

cnt=1
ans=1
for i in range(N-1):
    if Q[i]<Q[i+1]:
        cnt+=1
    else:
        cnt=1
    ans=max(cnt,ans)

print(N-ans)