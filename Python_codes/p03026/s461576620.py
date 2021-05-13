N=int(input())
G=[[] for _ in range(N)]
for _ in range(N-1):
    a,b=map(int, input().split())
    a,b=a-1,b-1
    G[a].append(b)
    G[b].append(a)
*C,=map(int, input().split())

C.sort(reverse=True)
ans=[-1]*N

stk=[0]
ans[0]=C[0]
idx=1
while stk:
    v=stk.pop()
    for to in G[v]:
        if ans[to]>0: continue
        ans[to]=C[idx]
        idx+=1
        stk.append(to)

print(sum(C)-C[0])
print(*ans)