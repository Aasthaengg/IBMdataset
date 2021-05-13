N, K = map(int,input().split())

#初期状態
node = [[] for _ in range(N)]
node[0] = [i for i in range(1,N)]

if K > N*(N-1)//2 - (N-1):
    print(-1)
else:
    cnt = 0
    for i in range(1,N):
        if cnt >= N*(N-1)//2-(N-1)-K:
            break
        for j in range(i+1,N):
            if cnt >= N*(N-1)//2-(N-1)-K:
                break
            node[i].append(j)
            cnt += 1
    
    print(N-1+cnt)
    for n in range(N):
        for t in node[n]:
            print(n+1,t+1)