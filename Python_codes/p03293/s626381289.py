S=input()
T=input()
A=[]
for i in range(len(S)):
    S=S[len(S)-1]+S[0:len(S)-1]
    A.append(S)
if T in A:
    print('Yes')
else:
    print('No')