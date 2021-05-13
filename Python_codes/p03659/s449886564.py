input()
cards = tuple(map(int, input().split(' ')))

a = sum(cards[1:])
s = cards[0]
diff_min = abs(a - s)

for card in cards[1:-1]:
    a -= card
    s += card
    diff_min = min(diff_min, abs(a - s))

print(diff_min)
