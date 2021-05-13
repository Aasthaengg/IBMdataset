from collections import deque

N, M = list(map(int, input().split()))

adjacency_list = [[] for i in range(N)]
for i in range(M):
    tmp = list(map(int, input().split()))
    adjacency_list[tmp[0] - 1].append(tmp[1] - 1)
    adjacency_list[tmp[1] - 1].append(tmp[0] - 1)
con_component = 0
# 接続確認
# print(adjacency_list)
visited_set = set(range(N))
queue = deque()
while visited_set:
    con_component += 1
    queue.append(visited_set.pop())
    while len(queue) != 0:
        ind = queue.popleft()
        # print("start queue", ind)
        for adjacency in adjacency_list[ind]:
            # print("aa",adjacency)
            if adjacency in visited_set:
                visited_set.remove(adjacency)
                queue.append(adjacency)
print(con_component - 1)
