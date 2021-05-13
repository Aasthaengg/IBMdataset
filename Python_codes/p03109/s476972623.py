S = input()

#print(int(S[5:7]))
if int(S[0:4]) < 2019:
    print('Heisei')

elif int(S[5:7]) < 4:
    print('Heisei')

elif int(S[5:7]) == 4 and int(S[8:10]) <= 30:
    print('Heisei')
else:
    print('TBD')