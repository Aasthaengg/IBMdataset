marks = ['S', 'H', 'C', 'D']
cards = {x:[0 for y in range(13)] for x in marks}

cnt = int(input())
while cnt > 0:
    values = input().split()
    cards[values[0]][int(values[1]) - 1] += 1
    cnt -= 1

for key in marks:
    for val in range(13):
        if 0 == cards[key][val]:
            print('{0} {1}'.format(key, val + 1))