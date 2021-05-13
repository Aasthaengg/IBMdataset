def slove():
    import sys
    import collections
    input = sys.stdin.readline
    n = int(input().rstrip('\n'))
    a = [list(map(int, input().rstrip('\n').split())) for _ in range(n)]
    ad = [0] * n
    dq = collections.deque([[0, i + 1] for i in range(n)])
    for i in range(10 ** 15):
        fd = {}
        while True:
            if len(dq) != 0:
                d, q = dq.popleft()
                q -= 1
                if d <= i:
                    if ad[q] < n - 1:
                        qq = a[q][ad[q]] - 1
                        tq = a[qq][ad[qq]] - 1
                        if q == tq and qq not in fd and tq not in fd:
                            ad[qq] += 1
                            ad[tq] += 1
                            if ad[qq] < n - 1:
                                dq.append([d + 1, qq + 1])
                            if ad[tq] < n - 1:
                                dq.append([d + 1, tq + 1])
                            fd[qq] = 0
                            fd[tq] = 0
                else:
                    dq.append([d, q + 1])
                    break
            else:
                break
        if len(dq) == 0:
            b = True
            for v in ad:
                if v != n - 1:
                    b = False
                    break
            if b:
                print(i + 1)
                exit()
            else:
                print(-1)
                exit()


if __name__ == '__main__':
    slove()
