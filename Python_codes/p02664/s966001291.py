T_list = input()
T = list(T_list)
nT = [0]*len(T)
if T[len(T)-1] == '?':
    T[len(T)-1] = 'D'
for i in range(len(T)):
    if T[i] != '?':
        nT[i] = T[i]
    else:
        if 0<i and i<len(T)-1:
            if T[i-1] == 'P':
                nT[i] = 'D'
                T[i] = 'D'
            elif T[i+1] == 'D':
                nT[i] = 'P'
                T[i] = 'P'
            elif T[i+1] == '?':
                nT[i] = 'P'
                T[i] = 'P'
            else:
                nT[i] = 'D'
                T[i] = 'D'
        else:
            if i<len(T)-1:
                if T[i+1] == 'D':
                    nT[i] = 'P'
                    T[i] = 'P'
                elif T[i+1] == '?':
                    nT[i] = 'P'
                    T[i] = 'P'
                else:
                    nT[i] = 'D'
                    T[i] = 'D'
nT=''.join(nT)              
print(nT)       