def main():
    from collections import deque, namedtuple
    from operator import attrgetter
    import sys
    input = sys.stdin.readline

    Mon = namedtuple('Mon', 'x h')  # 座標xにライフh
    Eff = namedtuple('Eff', 'x cnt')  # [,x]区間にcnt回爆発

    N, D, A = map(int, input().split())

    ms = []
    for _ in range(N):
        x, h = map(int, input().split())
        m = Mon(x=x, h=h)
        ms.append(m)

    ms.sort(key=attrgetter('x'))

    dq = deque()

    effect = 0
    cnt = 0
    for m in ms:
        while dq and dq[0].x < m.x:
            e = dq.popleft()
            effect -= e.cnt * A
        need_dmg = max(0, m.h - effect)
        if need_dmg:
            need_cnt = (need_dmg + A - 1) // A
            e = Eff(x=m.x + D * 2, cnt=need_cnt)
            dq.append(e)
            effect += need_cnt * A
            cnt += need_cnt
    print(cnt)


if __name__ == '__main__':
    main()

# import sys
#
# sys.setrecursionlimit(10 ** 7)
#
# input = sys.stdin.readline
# rstrip()
# int(input())
# map(int, input().split())
