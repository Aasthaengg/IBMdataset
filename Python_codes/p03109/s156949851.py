S = input()

year = int(S[0:4])
month = int(S[5:7])
day = int(S[8:])

if year<=2018:
    ans = 'Heisei'
elif year == 2019:
    if month<=4:
        ans = 'Heisei'
    else:
        ans = 'TBD'
else:
    ans = 'TBD'

print(ans)
