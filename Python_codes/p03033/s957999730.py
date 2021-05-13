def main():

    import sys
    import heapq

    N, Q = map(int, sys.stdin.readline().split())
    events = []

    for i in range(N):
        s, t, x = map(int, sys.stdin.readline().split())
        events.append((s - x, 1, x))  # 通行止め追加
        events.append((t - x, -1, x))  # 通行止め削除

    for i in range(Q):
        d = int(input())
        events.append((d, 2, 0))

    events.sort()
    events.append([float('inf'), 'guard', None])

    i = 0
    closing = set()
    hq = []  # 最小値を高速に入手するため
    while d >= events[i][0]:
        time, event, x = events[i]
        if event == 1:
            closing.add(x)
            heapq.heappush(hq, x)

        elif event == -1:
            closing.remove(x)

        else:
            while hq and (hq[0] not in closing):
                heapq.heappop(hq)

            if hq:
                print(hq[0])
            else:
                print(-1)

        i += 1


if __name__ == '__main__':
    main()
