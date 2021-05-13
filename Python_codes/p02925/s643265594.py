def resolve():
    N = int(input())
    A = []
    for _ in range(N):
        _a = list(map(lambda x: int(x)-1, input().split()))
        A.append(_a)
    ptrs = [0 for _ in range(N)]
    day = 0
    players = set([i for i in range(N)])
    finished = set()
    yest_players = set([i for i in range(N)])
    while True:
        todays_players = set()
        matched = False
        if len(finished) == N:
            break
        #print("------")
        for home in yest_players:
            if home in finished:
                continue
            away = A[home][ptrs[home]]
            if away in finished:
                continue
            #print(home, away)
            away_opp = A[away][ptrs[away]]
            if home in todays_players or away in todays_players:
                continue
            if home == away_opp:
                ptrs[home] += 1
                ptrs[away] += 1
                todays_players.add(home)
                todays_players.add(away)
                matched = True
                if ptrs[home] == N-1:
                    finished.add(home)
                if ptrs[away] == N-1:
                    finished.add(away)
        yest_players = todays_players
        #print(ptrs)
        if matched:
            day += 1
        else:
            day = -1
            break
    print(day)





if '__main__' == __name__:
    resolve()
