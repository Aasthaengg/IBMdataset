# A - Rainy Season

s = input()
for p in ('RRR', 'RR', 'R', ''):
    if p in s:
        print(len(p))
        exit()
