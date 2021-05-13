board = []

def detect():
    if sum([board[0], board[4], board[8]]) == 0:
        return True

    if sum([board[2], board[4], board[6]]) == 0:
        return True

    for i in range(3):
        if sum([board[i], board[i + 3], board[i + 6]]) == 0:
            return True

    for i in range(0, 3 * 3, 3):
        if sum([board[i], board[i + 1], board[i + 2]]) == 0:
            return True

    return False


for i in range(3):
    row = [int(v) for v in input().rstrip().split()]
    board.extend(row)


N = int(input().rstrip())
for i in range(N):
    b = int(input().rstrip())
    try:
        j =  board.index(b)
        board[j] = 0
    except ValueError:
        pass

r = 'Yes' if detect() else 'No'
print(r)

