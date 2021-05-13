n = int(input())
cards = [input() for _ in range(n)]
for suit in "SHCD":
    for rank in range(1, 14):
        if f'{suit} {rank}' not in cards:
            print(suit, rank)
