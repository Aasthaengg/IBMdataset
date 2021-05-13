n,t,aoki=map(int,input().split())

tree=[[] for _ in range(n)]

for _ in range(n-1):
    a,b=map(int,input().split())
    tree[a-1].append(b-1)
    tree[b-1].append(a-1)

if tree[t-1]==[aoki-1]:
    print(0)
    exit()


from collections import deque
ans=[-1]*n
stack = deque([t-1])
ans[t-1]=0

while len(stack)>0:
    tmp=stack.popleft()
    for item in tree[tmp]:
        if ans[item]==-1:
            ans[item]=ans[tmp]+1
            stack.append(item)


ans2=[-1]*n
stack = deque([aoki-1])
ans2[aoki-1]=0

result=0
#print("hoge",ans2)

while len(stack)>0:
    tmp=stack.popleft()
    for item in tree[tmp]:
        if ans2[item]==-1:
            ans2[item]=ans2[tmp]+1
            stack.append(item)
            if ans[item]<ans2[item]:
                result=max(result,ans2[item])-1
            elif ans[item]==ans2[item]:
                result=max(result,ans2[item])-1

print(result)





