T = list(input())

try:
    for i in range(len(T)):
        if T[i] == '?':
            if T[i-1] == 'P' or T[i-1] == 'D':
                T[i] = 'D'
            elif T[i-1] == 'D' and T[i+1] == '?':
                T[i] = 'P'
            else:
                T[i] = 'D'
except IndexError:
    T[-1] = 'D'


for t in T:
    print(t,end='')
