cards={}
for m in 'SHCD':
    for n in range(13):
        if m not in cards:
            cards[m] = {}
        cards[m][n+1] = False

c = input()
for i in range(int(c)):
    m, n = input().split()
    cards[m][int(n)] = True

for m in 'SHCD':
    for n in range(13):
        if not cards[m][n+1]:
            print(m, n+1)

