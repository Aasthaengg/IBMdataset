N,K=map(int,input().split())
s=input()
g=[]
l=0
for i in range(1,N):
    if s[i]!=s[i-1]:
        g.append(i-l)
        l=i
g.append(N-l)

M=len(g)
ans=0
S=[0]
for h in range(M):
    S.append(S[h]+g[h])

if s[0]=="0":
    if K>M//2:
        print(N)
    else:
        for j in range(M):
            if j+2*K+1>M:
                break
            elif j==0:
                ans=max(ans,S[j+2*K]-S[j])
            elif j%2==1:
                ans=max(ans,S[j+2*K+1]-S[j])
        ans=max(ans,S[M]-S[M-2*K])
        print(ans)
    
else:
    if K>=M//2+M%2:
        print(N)
    else:
        for j in range(M):
            if j+2*K+1>M:
                break
            elif j%2==0:
                ans=max(ans,S[j+2*K+1]-S[j])
        ans=max(ans,S[M]-S[M-2*K])
        print(ans)