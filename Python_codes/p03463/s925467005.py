N, A, B = map(int, input().split())
blocks_between_AB = B-A-1

if blocks_between_AB%2 == 0:
    winner = "Borys"
else:
    winner = "Alice"

print(winner)