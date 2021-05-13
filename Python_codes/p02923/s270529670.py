n = int(input())
h = list(map(int, input().split()))

max_moves = 0
for i in range(n):
    if i == 0:
        moves = 0
    elif h[i - 1] < h[i]:
        moves = 0
    else:
        moves += 1
    max_moves = max(max_moves, moves)
print(max_moves)
