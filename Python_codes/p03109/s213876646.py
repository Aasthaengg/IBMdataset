s = input()

year = s[:4]
month = s[5:7]
day = s[8:10]

a_day = int(year + month + day)

if 20190430 < a_day:
    print('TBD')
else:
    print('Heisei')