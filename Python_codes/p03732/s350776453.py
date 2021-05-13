from collections import deque
N,W=map(int,input().split())
w1,v1=map(int,input().split())
V=[[v1],[],[],[]]
for i in range(N-1):
    w,v=map(int,input().split())
    V[w-w1].append(v)
for i in range(4):
    V[i].sort(reverse=True)
W0=W
V0=0
ans=0
for a in range(-1,len(V[0])):
    if a!=-1:
        W0-=w1
        if W0<0:
            break
        V0+=V[0][a]
    W1=W0
    V1=V0
    ans=max(ans,V0)
    for b in range(-1,len(V[1])):
        if b!=-1:
            W1-=w1+1
            if W1<0:
                break
            V1+=V[1][b]
        W2=W1
        V2=V1
        ans=max(ans,V1)
        for c in range(-1,len(V[2])):
            if c!=-1:
                W2-=w1+2
                if W2<0:
                    break
                V2+=V[2][c]
            ans=max(ans,V2)
            if W2//(w1+3)>0:
                ans=max(ans,V2+sum(V[3][0:(W2//(w1+3))]))
print(ans)