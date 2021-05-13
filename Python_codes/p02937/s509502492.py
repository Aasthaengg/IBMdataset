import bisect
S=list(input())
T=list(input())

N=len(S)
p=[[] for _ in range(26)]
for i in range(N):
    p[ord(S[i])-97].append(i+1)

res=0
b=0
for t in T:
    k=ord(t)-97
    if len(p[k])==0:
        print(-1)
        exit()
    r=bisect.bisect_right(p[k],b)
    if len(p[k])>r:
        res+=p[k][r]-b
        b=p[k][r]
    else:
        res+=N-b+p[k][0]
        b=p[k][0]

print(res)