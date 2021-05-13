n = int(input())
all_cards = [i + " " + str(j) for i in ['S', 'H', 'C', 'D'] for j in range(1, 14)]
for i in range(n):
    all_cards.remove(input())
for i in all_cards:
    print(i)