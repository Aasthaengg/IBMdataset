S = input()
if int(S[:4]) == 2019:
    if int(S[5:7]) == 4:
        if int(S[8:-1]) == 30:
            print('Heisei')
        elif int(S[8:-1]) >= 31:
            print('TBD')
        else:
            print('Heisei')
    elif int(S[5:7]) >= 5:
        print('TBD')
    else:
        print('Heisei')
elif int(S[:4]) >= 2020:
    print('TBD')
else:
    print('Heisei')
