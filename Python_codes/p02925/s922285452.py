def solve():
    N = int(input())
    tournament = [list(map(lambda x:int(x)-1, input().split())) for _ in range(N)]
    map_que_tournament = {i:[] for i in range(N)} # player iがjと戦いたがってる
    competition_num = -1
    que_player = list(range(N))
    
    while que_player:
        day_process_flag = False
        new_queue = []
        # print(que_player)
        for player in que_player:
            if tournament[player]:
                match_player = tournament[player].pop(0)
                # ぶじマッチング相手が見つかったら
                if map_que_tournament[match_player] and player == map_que_tournament[match_player][0]:
                    # print(player, match_player)
                    day_process_flag = True
                    new_queue.append(match_player)
                    new_queue.append(player)
                    map_que_tournament[match_player].pop()
                else:
                    map_que_tournament[player].append(match_player)

        if day_process_flag:
            if competition_num < 0:
                competition_num = 1
            else: competition_num += 1

        que_player = new_queue
        
    # 途中でやめた場合
    for t in tournament:
        if t:
            competition_num = -1
            break

    print(competition_num)
    
solve()