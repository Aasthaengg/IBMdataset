N,M=map(int,input().split())
L=[]

for i in range(M):
    m=list(map(int,input().split()))
    L.append(m[1:])

#print(L)

S=list(map(int,input().split()))

ans=0

for i in range(2**N):
    sw=[0 for i in range(M)]
    I=i+0
    for j in range(N):
        if I&1==True:
            for k in range(M):
                if j+1 in L[k]:
                    sw[k]+=1
        I=I>>1
    #print(sw)
    cnt=0
    for j in range(M):
        if sw[j]%2==S[j]:
            cnt+=1
    if cnt==M:
        ans+=1
print(ans)