N=int(input())
F=[list(input().split()) for _ in range(N)]
P=[list(map(int, input().split())) for _ in range(N)]

ans=[]
for i in range(1,2**10):
    tmp=0
    for j in range(N):
        b=''.join(F[j])
        ct=0
        for k in range(10):
            if (i>>k)&int(b[k]):
                ct+=1
        tmp+=P[j][ct]
    ans.append(tmp)
print(max(ans))