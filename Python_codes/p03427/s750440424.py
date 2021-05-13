N=input()

S=[-1]*len(N)
for i in range(len(N)):
    S[i]=int(N[i])

if sum(S[1:])== 9*(len(S)-1):
    print(sum(S))
else:
    print(9*(len(S)-1) + (S[0]-1))