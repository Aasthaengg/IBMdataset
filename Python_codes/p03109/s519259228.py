S = input()
Sint = int(S[:4])*10000 + int(S[5:7])*100 + int(S[8:])
if Sint > 20190430:
    print('TBD')
else:
    print('Heisei')
