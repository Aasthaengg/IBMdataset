# ABC119
S = input()
if int(S[0:4]) > 2019:
    print('TBD')
    exit()
elif int(S[0:4]) == 2019:
    if int(S[5:7]) >= 5:
        print('TBD')
        exit()
print('Heisei')
