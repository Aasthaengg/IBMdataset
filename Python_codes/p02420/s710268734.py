deck, h = ([], [])
while True:
    temp = []
    deck.append(list(input().strip()))
    if deck[-1][0] == '-':
        del deck[-1]
        break
    m = int(input())
    for i in range(m):
        temp.append(int(input()))
    else:
        h.append(temp)

for j in range(len(deck)):
    for k in h[j]:
        for l in deck[j][:k]:
            deck[j].append(l)
        del deck[j][:k]

    [print(v, end='') for v in deck[j]]
    print()