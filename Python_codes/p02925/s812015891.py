def resolve():
    N = int(input())
    A = [list(map(lambda x:int(x)-1,input().split())) for _ in range(N)]
    cur = [0 for _ in range(N)]
    yesterday = set(range(N))
    rest = N * (N-1)
    day = 0
    while len(yesterday) > 0 and rest > 0:
        today = set()
        totoday = set()
        for y in yesterday:
            o = A[y][cur[y]]
            if A[o][cur[o]] == y:
                today.add(o)
                today.add(y)
        for t in today:
            cur[t] += 1
            if cur[t] < N-1:
                totoday.add(t)
        rest -= len(today)
        yesterday = totoday
        day += 1
    if rest == 0:
        print(day)
    else:
        print(-1)
resolve()