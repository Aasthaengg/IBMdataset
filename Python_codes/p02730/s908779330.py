S=input()
T=S[:(len(S)-1)//2]
U=S[(len(S)+3)//2-1:]
if S==S[::-1]:
    if T==T[::-1]:
        if U==U[::-1]:
            print('Yes')
        else:print('No')
    else:print('No')
else:print('No')