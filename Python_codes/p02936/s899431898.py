n,q = map(int,input().split())
tree = [[] for _ in range(n)]
for i in range(n-1):
    a,b = map(lambda x: int(x)-1, input().split())
    tree[a].append(b)
    tree[b].append(a)

w = [0]*n
for i in range(q):
    p,x = map(int,input().split())
    w[p-1] += x

stack = [0]
flag = [False]*n

while stack:
    nex = stack.pop()
    flag[nex] = True
    for i in tree[nex]:
        if flag[i]:
            continue
        w[i] += w[nex]
        stack.append(i)

print(*w)