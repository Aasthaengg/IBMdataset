T = str(input())
T=list(T)
if not T[0]=='?':
    for i in range(1,len(T)-1):
        if T[i]=='?':
            if T[i-1]=='D' and T[i+1]=='D':
                T[i]='P'
            else:
                T[i]='D'
    if T[len(T)-1]=='?':
        T[len(T)-1]='D'
else:
    T[0]='D'
    for i in range(1,len(T)-1):
        if T[i]=='?':
            if T[i-1]=='D' and T[i+1]=='D':
                T[i]='P'
            else:
                T[i]='D'
    if T[len(T)-1]=='?':
        T[len(T)-1]='D'

print(''.join(T))