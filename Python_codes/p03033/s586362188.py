# https://atcoder.jp/contests/abc128/submissions/11722664

def main():
    from collections import deque, namedtuple
    from heapq import heappush, heappop
    from operator import attrgetter
    import sys

    input = sys.stdin.readline
    Event = namedtuple('Event', 'pos start end')
    UC = namedtuple('UC', 'pos end')  # UnderConstruction

    N, Q = map(int, input().split())

    events = []
    for _ in range(N):
        s, t, x = map(int, input().split())
        e = Event(pos=x, start=s - x, end=t - x)  # 時間[s-x,t-x)にpos=0にいるとpos=xで工事中
        events.append(e)
    events.sort(key=attrgetter('start'))
    events = deque(events)

    D = (int(input()) for _ in range(Q))

    ans = []
    h = []
    for d in D:
        while events and events[0].start <= d:
            e = events.popleft()
            heappush(h, UC(pos=e.pos, end=e.end))

        while h and h[0].end <= d:
            heappop(h)

        ans.append(h[0].pos if h else -1)

    print(*ans, sep='\n')


if __name__ == '__main__':
    main()
