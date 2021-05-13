from collections import deque
import copy

# グラフの作成(無向グラフでは#を消す)
n, q = map(int, input().split())
graph = [deque([]) for _ in range(n+1)]
for _ in range(n-1):
    a, b  = [int(x) for x in input().split()]
    graph[a].append(b)
    graph[b].append(a) # 無向グラフ
#print(graph)
q_sum_list = [0 for _ in range(n)]
for i in range(q):
    p, x = map(int, input().split())
    q_sum_list[p-1] += x
#print(q_sum_list)
arrive_rireki = [-1] * (n + 1)

score = [0]*n
score_temp = 0

# 深さ優先探索
def dfs(v):
    global score_temp
    stack = [v]
    arrive_rireki[v] = 1
    score_temp += q_sum_list[v-1]
    while stack:
        v = stack[-1]
        if graph[v]:
            w = graph[v].popleft()
            if arrive_rireki[w] < 0:
                arrive_rireki[w] = 1
                stack.append(w)
                score_temp += q_sum_list[w-1]
        else:
            stack.pop()
            score[v-1] = score_temp
            score_temp -= q_sum_list[v-1]
    return score

dfs(1)
#print(eda_list)
print(* score)
