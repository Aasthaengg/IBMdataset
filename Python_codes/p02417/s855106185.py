import sys

charas = 'abcdefghijklmnopqrstuvwxyz'

data = []
for line in sys.stdin:
    data.append(line)
for chara in charas:
    cnt = 0
    for row in data:
        cnt += row.count(chara)
        cnt += row.count(chara.upper())
    print('{} : {}'.format(chara, cnt))