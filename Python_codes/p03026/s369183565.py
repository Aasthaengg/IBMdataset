N=int(input())
AB=[list(map(int,input().split())) for i in range(N-1)]
C=list(map(int,input().split()))
C.sort(reverse=True)
data=[[] for i in range(N+1)]
num=[-1 for i in range(N+1)]
num[1]=C[0]
for a,b in AB:
    data[a].append(b)
    data[b].append(a)
sumc=sum(C[1:])

stack=[1]
visited=set()
visited.add(1)
idx=1
while stack:
    a=stack.pop()
    for p in data[a]:
        if not p in visited:
            visited.add(p)
            num[p]=C[idx]
            idx+=1
            stack.append(p)
print(sumc)
print(" ".join([str(num[i]) for i in range(1,N+1)]))
