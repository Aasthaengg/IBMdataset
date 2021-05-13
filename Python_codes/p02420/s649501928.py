cards = []
nums = []
while True:
    card = raw_input()
    if card == '-': 
        break   
    cards += [card]
    n = 0   
    for _ in range(int(raw_input())):
        n += int(raw_input())
    nums += [n]

for c, n in zip(cards, nums):
    w = c * ((max(len(c), n)/n)+10)
    print w[n:n+len(c)]