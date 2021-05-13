s = input()
ans = 'TBD'
if int(s[:4]) < 2019:
    ans = 'Heisei'
elif int(s[5:7]) <= 4:
    ans = 'Heisei'
print(ans)
