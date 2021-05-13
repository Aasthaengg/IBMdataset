N=int(input())
S=[input() for i in range(3)]
ans=0
for i in range(N):
    s=set([S[j][i] for j in range(3)])
    ans+=len(s)-1
print(ans)