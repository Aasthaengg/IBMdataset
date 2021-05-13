S = input()
Flag = False
if (S[0]=='A') and S[2:len(S)-1].count('C')==1:
    ReS = S.replace('C','')[1:]
    if ReS.islower():
        Flag = True
if Flag:
    print('AC')
else:
    print('WA')
