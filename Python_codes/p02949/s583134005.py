N,M,P = map(int,input().split())

edge_dic = {}

for _ in range(M):
    A,B,C = map(int,input().split())
    if not A - 1 in edge_dic:
        edge_dic[A-1] = [[B-1,C-P]]
    else:
        edge_dic[A-1].append([B-1,C-P])

# print(edge_dic)

INF = 10 ** 10

ans_array = [-INF] * N
can_visit = [0] * N
ans_array[0] = 0
can_visit[0] = 1 
last_ans_change = -1

for i in range(N*2):
    change_flag = 0
    for key, value in edge_dic.items():
        if can_visit[key] == 0:
            continue
        for v in value:
            goal, cost = v
            if ans_array[goal] < ans_array[key] + cost:
                ans_array[goal] = ans_array[key] + cost
                if i >= N:
                    ans_array[goal] = INF
                can_visit[goal] = 1
                change_flag = 1
                if goal == N - 1:
                    last_ans_change = i
                    if i >= N:
                        print(-1)
                        exit()
    if change_flag == 0:
        break


ans = max(0,ans_array[N-1])

print(ans)