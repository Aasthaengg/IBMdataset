from collections import defaultdict, deque

def resolve():
    n, m = map(int, input().split())
    aisle = defaultdict(list)
    for _ in range(m):
        a, b = map(int, input().split())
        aisle[a - 1].append(b - 1)
        aisle[b - 1].append(a - 1)

    d = deque()
    d.append(0)

    room_depths = [-1] * 100010
    room_depths[0] = 0
    room_inds = [-1] * 100010

    # BFS
    while d:
        room = d.popleft()
        for next_room in aisle[room]:

            # 隣接する頂点で、まだ数字が書かれていない頂点に、現在の頂点の数字+1を書く
            if room_depths[next_room] == -1:
                d.append(next_room)
                room_depths[next_room] = room_depths[room] + 1
                room_inds[next_room] = room + 1

    print('Yes')
    for i in range(1, n):
        print(room_inds[i])
        
resolve()