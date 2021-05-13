S = input()
if 'W' not in S:
    print(0)
elif 'B' not in S:
    print(0)
else:
    if S[0] == 'B':
        count = S.count('BW')
        if S[-1] == 'B':
            print(count*2)
        else:
            print(count*2 - 1)
    else:
        count = S.count('WB')
        if S[-1] == 'W':
            print(count*2)
        else:
            print(count*2 - 1)