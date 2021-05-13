n = int(input())
a = set([])
for _ in range(n):
    a.add(input())
for suit in ('S', 'H', 'C', 'D'):
    for i in range(1,14):
        card = suit + ' ' + str(i)
        if card not in a:
            print(card)
