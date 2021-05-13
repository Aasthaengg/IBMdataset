s = input()
a = s.split('/')

if int(a[0]) < 2019:
    print('Heisei')
elif int(a[1]) <= 4:
    print('Heisei')
else:
    print('TBD')