S = input()
T = input()
if len(S)==1:
    Flag = (S==T)
else:
    Flag = False
    for X in range(0,len(S)):
        S = S[-1]+S[0:-1]
        if S==T:
            Flag = True
            break
if Flag:
    print('Yes')
else:
    print('No')