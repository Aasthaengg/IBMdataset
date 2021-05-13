def solve():
    S = input()
    X,Y = map(int, input().split())
    
    S_F = S.split('T')
    move_x = list(map(len, S_F[::2]))
    move_y = list(map(len,S_F[1::2]))
    
    if move_x:
        X -= move_x[0]
        move_x = move_x[1:]
    
    # たどりつけない場合
    if sum(move_x) < abs(X) or sum(move_y) < abs(Y):
        print('No')
        return
    
 
    move_x_process = [mx for mx in move_x if mx > 0]
    move_y_process = [my for my in move_y if my > 0]
    X = abs(X); Y = abs(Y)
    len_move_x = len(move_x_process)
    sum_x = sum(move_x_process)
    len_move_y = len(move_y_process)
    sum_y = sum(move_y_process)
 
    dp_table = [[False for _ in range(sum_x+1)] for _ in range(len_move_x+1)]
    dp_table[0][0] = True
    
    for i in range(0,len_move_x):
        for j in range(0, sum_x+1):
            dp_table[i+1][j] = dp_table[i][abs(j-move_x_process[i])]
            if j+move_x_process[i] <= sum_x: 
                dp_table[i+1][j] = dp_table[i+1][j] or dp_table[i][j+move_x_process[i]]
    
    # print(dp_table)
    ret = dp_table[len_move_x][X]
    dp_table = [[False for _ in range(sum_y+1)] for _ in range(len_move_y+1)]
    dp_table[0][0] = True
    for i in range(0,len_move_y):
        for j in range(0, sum_y+1):
            # if j-move_x_process[i] >= 0:
            dp_table[i+1][j] = dp_table[i][abs(j-move_y_process[i])]
            if j+move_y_process[i] <= sum_y:
                dp_table[i+1][j] = dp_table[i+1][j] or dp_table[i][j+move_y_process[i]]
    
    ret = ret and dp_table[len_move_y][Y]
    print('Yes' if ret else 'No')
    
solve()