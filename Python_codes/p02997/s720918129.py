N, K = map(int,input().split())
max_edge = (N-1)*(N-2)//2
all_edges = [[i,j] for i in range(N) for j in range(i+1,N)]

if 0 <= K <= max_edge:
    minus = max_edge - K
    count = 0
    answer = []
    for edge in all_edges:
        if edge[0] == 0:
            answer.append(edge)
        elif count < minus:
            answer.append(edge)
            count+=1
    print(len(answer))
    for i in range(len(answer)):
        print((" ").join(str(j+1) for j in answer[i]))
else:
    print(-1)