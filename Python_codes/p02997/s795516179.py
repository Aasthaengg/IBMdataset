N, K = map(int, input().split())

if K > (N-1)*(N-2)//2:
    print(-1)
else:
    ans = []
    for i in range(N - 1):
        ans.append([i+1, N])
    add = (N-1)*(N-2)//2 - K
    edge = []
    for i in range(N - 1):
        for j in range(i):
            edge.append([i+1, j+1])
    for i in range(add):
        ans.append(edge[i])
    print(len(ans))
    for i in ans:
        print(i[0], end=' ')
        print(i[1])