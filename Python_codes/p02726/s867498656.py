from collections import deque

N,X,Y= map(int,input().split())

root = [[] for i in range(N)]
for i in range(N-1):
    root[i].append(i+1)
    root[i+1].append(i)

root[X-1].append(Y-1)
root[Y-1].append(X-1)

ans = [0]*(N-1)

for i in range(N):
    stack=deque([i])
    check = [-1]*N
    check[i] = 0

    while len(stack)>0:
        v = stack.popleft()
        for i in root[v]:
            if check[i] == -1:
                check[i]=check[v]+1
                stack.append(i)
    #print(check)
    for ch in check:
        if ch > 0:
            ans[ch-1] += 1

for aa in ans:
    print(aa//2)
