S = list(map(int,input().rstrip().split('/')))
if S[0]>2019:
    print('TBD')
elif S[0]==2019:
    if S[1]>4:
        print('TBD')
    elif S[1]==4:
        if S[2]>30:
            print('TBD')
        else:
            print('Heisei')
    else:
        print('Heisei')
else:
    print('Heisei')