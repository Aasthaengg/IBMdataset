N=int(input())
E=[[] for _ in range(N)]
for _ in range(N-1):
    a,b=map(lambda x:int(x)-1, input().split())
    E[a].append(b)
    E[b].append(a)
C=list(map(int, input().split()))

C.sort(reverse=True)

ans=[0]*(N)
stack=[0]
ans[0]=C[0]
k=1
while stack:
    n=stack.pop()
    for to in E[n]:
        if ans[to]!=0: continue
        ans[to]=C[k]
        k+=1
        stack.append(to)

print(sum(C[1:]))
print(' '.join(map(str,ans)))