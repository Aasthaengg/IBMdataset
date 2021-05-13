N,K = map(int,input().split())
if K > (N-1)*(N-2)//2:
    print(-1)
else:
    edges = []
    for i in range(2,N+1):
        edges.append((1,i))
    cur = (N-1)*(N-2)//2
    if cur > K:
        for i in range(2,N+1):
            for j in range(2,N+1):
                if i > j:
                    edges.append((i,j))
                    cur -= 1
                    if cur == K:
                        break
            else:
                continue
            break
    print(len(edges))
    for i,j in edges:
        print(i,j)
