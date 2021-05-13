T=input()
N=len(T)
poe=[]
for i in range(N):
    poe.append(T[i])
for i in range(N):
    if T[i]=='?':
        poe[i]='D'

print(''.join(poe))