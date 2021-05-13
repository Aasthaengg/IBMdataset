def isReach( goal, move, is_x):
    msum = sum(move)
    m = len(move)

    if msum < abs(goal):
        return False

    dp = [[False for _ in range(msum*2+1)] for _ in range(m+1)]
    dp[0][0] = True
    
    for i in range(m):
        for j in range(-msum,msum+1):
            if i == 0 and dp[i][j] and is_x:
                dp[i+1][j+move[i]] = True
            elif dp[i][j]:
                dp[i+1][j-move[i]] = True
                dp[i+1][j+move[i]] = True
    
    return dp[m][goal]


s = list( input().split('T') )
x,y = map( int, input().split() )

move_dist = [len(move) for move in s]
x_move = move_dist[0::2]
y_move = move_dist[1::2]

if isReach(x,x_move,True) and isReach(y,y_move,False):
    print('Yes')
else:
    print('No')