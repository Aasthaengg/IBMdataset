from collections import deque

N = int(input())

neighbor = [[] for _ in range(N)]

for _ in range(N-1):
    a, b = map(int, input().split())
    neighbor[a-1].append(b-1)
    neighbor[b-1].append(a-1)

# 黒を0、白を1、未着色を-1で表す
black_white = [0] + [-1]*(N-2) + [1]

# 点iを与えると、点iからの最短距離のリストを返す
def shortest_distance(home_point):
    shortest_distance_list = [-1]*N
    shortest_distance_list[home_point] = 0
    next_points = deque([home_point])

    while len(next_points) > 0:
        p = next_points.popleft()
        for idx in neighbor[p]:
            if shortest_distance_list[idx] == -1:
                shortest_distance_list[idx] = shortest_distance_list[p]+1
                next_points.append(idx)

    return shortest_distance_list

shortest_distance_from_Fennec = shortest_distance(0)
shortest_distance_from_Snuke = shortest_distance(N-1)

for idx in range(1,N-1):
    if shortest_distance_from_Fennec[idx] <= shortest_distance_from_Snuke[idx]:
        black_white[idx] = 0
    else:
        black_white[idx] = 1

print("Fennec" if black_white.count(0) > black_white.count(1) else "Snuke")
