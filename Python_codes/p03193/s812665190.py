N,H,W=map(int,input().split(' '))
boards=[list(map(int,input().split(' '))) for i in range(N)]
print(len([1 for board in boards if board[0]>=H and board[1]>=W]))