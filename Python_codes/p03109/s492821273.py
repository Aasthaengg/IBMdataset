year, month, day = map(int, input().split('/'))
if year <= 2019 and month <= 4 and day <= 30:
    print('Heisei')
else:
    print('TBD')