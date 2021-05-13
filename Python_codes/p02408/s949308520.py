total_card = []
for flower in 'SHCD':
    for num in range(1, 14):
        total_card.append((flower, num))

current_card = []
k = int(raw_input())
for i in range(k):
    f, v = map(str, raw_input().split())
    t = (f, int(v))
    current_card.append(t)


loss_card = []
for tu in total_card:
    if tu not in current_card:
        loss_card.append(tu)

for tu in loss_card:
    print tu[0] + ' ' + str(tu[1])