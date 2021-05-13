from collections import deque, defaultdict

N, M, P = map(int, input().split())

edge_dic = defaultdict(lambda: [])
reverse_edge_dic = defaultdict(lambda: [])

for _ in range(M):
    A, B, C = map(int, input().split())
    # if not A - 1 in edge_dic:
    #     edge_dic[A-1] = [[B-1, C-P]]
    # else:
    edge_dic[A-1].append([B-1, C-P])
    # if not B - 1 in reverse_edge_dic:
    #     reverse_edge_dic[B-1] = [[A-1, C-P]]
    # else:
    reverse_edge_dic[B-1].append([A-1, C-P])

# print(edge_dic)

INF = 10 ** 10

ans_array = [-INF] * N
ans_array[0] = 0

for i in range(N+1):
    change_flag = 0
    for key, value in edge_dic.items():
        for v in value:
            goal, cost = v
            if ans_array[goal] < ans_array[key] + cost:
                ans_array[goal] = ans_array[key] + cost
                change_flag = 1
    if change_flag == 0:
        break
else:
    forward_set = set()
    node_deque = deque()
    node_deque.append(0)
    forward_set.add(0)
    while len(node_deque):
        edge = node_deque.pop()
        for v in edge_dic[edge]:
            goal, cost = v
            if goal not in forward_set:
                forward_set.add(goal)
                node_deque.append(goal)

    backward_set = set()
    node_deque = deque()
    node_deque.append(N-1)
    backward_set.add(N-1)
    while len(node_deque):
        edge = node_deque.pop()
        for v in reverse_edge_dic[edge]:
            goal, cost = v
            if goal not in backward_set:
                backward_set.add(goal)
                node_deque.append(goal)
    can_use = forward_set & backward_set
    # print(forward_set, backward_set, can_use)

    new_edge_dic = {i: edge_dic[i] for i in can_use}

    ans_array = [-INF] * N
    ans_array[0] = 0
    for i in range(len(can_use)+1):
        change_flag = 0
        for key, value in new_edge_dic.items():
            for v in value:
                goal, cost = v
                if ans_array[goal] < ans_array[key] + cost:
                    ans_array[goal] = ans_array[key] + cost
                    change_flag = 1
        if change_flag == 0:
            break
    else:
        print(-1)
        exit()
    
ans = max(0, ans_array[N-1])
print(ans)
