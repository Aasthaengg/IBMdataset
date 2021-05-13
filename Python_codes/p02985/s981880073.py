import sys
input=sys.stdin.readline

mod=10**9+7
MAX=10**5+100

g1=[1,1]
g2=[1,1]
for i in range(2,MAX+1):
    num_1=g1[-1]*i%mod
    g1.append(num_1)
    g2.append(pow(num_1,mod-2,mod))

    
N,K=map(int,input().split())
AB=[list(map(int,input().split())) for i in range(N-1)]

data=[[] for i in range(N+1)]
for A,B in AB:
    data[A].append(B)
    data[B].append(A)
    
count=[0]*(N+1)
flag=[0]*(N+1)
que=[1]
flag[1]=1
while que:
    h=[]
    for u in que:
        cnt=0
        for v in data[u]:
            if flag[v]==0:
                flag[v]=1
                cnt+=1
                h.append(v)
        count[u]=cnt
    que=h

if K-1-count[1]<0:
    print(0)
    sys.exit()
ans=K*g1[K-1]*g2[K-1-count[1]]%mod

for i in range(2,N+1):
    if count[i]==0:
        continue
    else:
        if K-2-count[i]<0:
            print(0)
            sys.exit()
        ans=ans*g1[K-2]*g2[K-2-count[i]]%mod
    
print(ans)