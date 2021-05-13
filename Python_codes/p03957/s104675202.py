S=input()

nc=-1
nf=-1
for i in range(len(S)):
    if S[i]=='C':
        nc=i
        break
for i in range(len(S)):
    if S[i]=='F':
        nf=i

print('Yes' if nc < nf and nc>=0 and nf>=1 else 'No')