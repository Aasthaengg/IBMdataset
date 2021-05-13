s = str(input())

year = ''
for i in range(4):
    y = s[i]
    flag1 = True
    if y == '0':
        if len(year) == 0:
            flag1 = False
        if flag1:
            year += y
    else:
        year += y
year = int(year)

month = ''
for i in range(5, 7):
    m = s[i]
    if i == 5 and m == '0':
        continue
    else:
        month += m
month = int(month)


if year < 2019:
    answer = 'Heisei'

elif year == 2019 and month <= 4:
    answer = 'Heisei'

else:
    answer = 'TBD'

print(answer)