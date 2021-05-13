n=int(input())

tree=[[] for _ in range(n)]

for _ in range(n-1):
    a,b=map(int,input().split())
    tree[a-1].append(b-1)
    tree[b-1].append(a-1)

ans=[0]*n
ans[0]="B"
ans[n-1]="W"

from collections import deque

stack = deque([0,n-1])

while len(stack)>1:
    tmp=stack.popleft()

    for item in tree[tmp]:
        if ans[item]==0:
            if ans[tmp]=="W":
                ans[item]="W"
            else:
                ans[item]="B"
            stack.append(item)

if ans.count("B")>ans.count("W"):
    print("Fennec")
else:
    print("Snuke")

