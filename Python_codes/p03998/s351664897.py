card = {}
card['a'] = list(input())
card['b'] = list(input())
card['c'] = list(input())

crd = 'a'

while True:
    crd = card[crd].pop(0)

    if len(card[crd]) == 0:
        break

print(crd.upper())