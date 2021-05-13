S = input()

if int(S[0:4]) <= 2018 or (int(S[0:4]) == 2019 and int(S[5:7]) < 5):
    print('Heisei')
else:
    print('TBD')
