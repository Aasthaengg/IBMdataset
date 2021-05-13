N = int(input())

Edge = [[]for _ in range(N)]
Num = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int,input().split())
    a -= 1
    b -= 1
    Edge[a].append(b)
    Edge[b].append(a)
for _ in range(N):
    Num[len(Edge[_])].append(_)
C = list(map(int, input().split()))
C.sort()
cnt = 0
Ans = [-1] * N
ans = 0
for i in range(1, N):
    if cnt == N:
        break
    while Num[i]:
        if Num[0]:
            Ans[Num[0][0]] = C[cnt]
            cnt += 1
        x = Num[i].pop()
        if Ans[x] != -1:
            continue
        Ans[x] = C[cnt]
        ans += C[cnt] * i
        cnt += 1
        for y in Edge[x]:
            num = len(Edge[y])
            Num[num-1].append(y)
            Edge[x].remove(y)
            Edge[y].remove(x)

print(ans)
for i, a in enumerate(Ans):
    if i == N-1:
        print(a)
    else:
        print(a, end=' ')
