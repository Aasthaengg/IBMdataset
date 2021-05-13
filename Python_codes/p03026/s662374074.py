from collections import deque
N=int(input())
tree=[[] for _ in range(N)]
tree2=[]
for i in range(N-1):
    a,b=map(int,input().split())
    tree[a-1].append(b-1)
    tree[b-1].append(a-1)
    tree2.append([a-1,b-1])
score=list(map(int,input().split()))
score.sort(reverse=True)
#print(tree,tree2,score)
v=0
d=deque()
seen=[0]*N
d.append(v)
ans=[]
l=[0]*N
s=0
while len(ans)!=N:
    v=d.popleft()
    seen[v]=1
    ans.append(v)
    for j in tree[v]:
        if seen[j]!=1:
            d.append(j)
    #print(ans,seen)
    #input()
for i in range(N):
    l[ans[i]]=score[i]
#print(l)
for i in range(N-1):
    s=s+min(l[tree2[i][0]],l[tree2[i][1]])
print(s)
print(*l,sep=" ")


