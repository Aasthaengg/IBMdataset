board = list(map(int, input().split()))
k = int(input())
sort_board = sorted(board, reverse=True)
for _ in range(k):
    sort_board[0] *= 2
print(sum(sort_board))