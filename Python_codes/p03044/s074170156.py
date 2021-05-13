from collections import deque


n = int(input())
e = {}
for i in range(n-1):
    u,v,w = map(int,input().split())
    if u not in e:
        e[u] = [[v,w]]
    else:
        e[u].append([v,w])

    if v not in e:
        e[v] = [[u,w]]
    else:
        e[v].append([u,w])


que = deque()
que.append([1,0,0])
ans = [-1 for i in range(n)]
ans[0] = 0
no_one = True
flag = True
while True:
    if len(que) == 0:
        break
    top = que.popleft()
    st = top[0]
    for edge in e[st]:
        ecos = edge[1]
        nex = edge[0]
        if ans[nex-1] == -1:
            cos0 = top[1]+ecos
            cos1 = top[2]+ecos

            if cos0 %2 == 0:
                que.append([nex,0,cos1])
                ans[nex-1] = 0
            elif cos1 %2 == 0:
                que.append([nex,cos0,0])
                ans[nex-1] = 1
            else:
                if no_one:
                    que.append([nex, cos0, 0])
                    ans[nex - 1] = 1
                else:
                    flag = False
                    break

    if not flag:
        break
    # print(que)

for a in ans:
    print(a)
# print(ans)