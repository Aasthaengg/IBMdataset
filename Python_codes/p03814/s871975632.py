S = input()

N = len(S)
Aflag = -1
Zflag = 0
for i in range(N):
    if Aflag == -1 and S[i] == 'A':
        Aflag = i
    elif S[i] == 'Z':
        Zflag = i

print(Zflag-Aflag+1)
