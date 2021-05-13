n,k = map(int, input().split())

graph = [[] for i in range(n)]
if k > ((n-1)*(n-2))//2:
    print(-1)
else:
    for i in range(1,n):
        graph[0].append(i+1)
    
    remain = ((n-1)*(n-2))//2 - k
    for i in range(1,n):
        if remain <= 0:
            break
        for j in range(i+1,n):
            if remain > 0:
                graph[i].append(j+1)
                remain -= 1
            else:
                break

    print(((n-1)*(n-2))//2 - k + (n-1))
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            print(i+1, graph[i][j])


