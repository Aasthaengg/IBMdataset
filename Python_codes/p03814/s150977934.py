S=input()
i=S.index('A')
T=S[::-1]
j=len(S)-T.index('Z')
print(j-i)