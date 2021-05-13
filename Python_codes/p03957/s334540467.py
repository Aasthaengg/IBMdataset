S=list(str(input()))
c=0
for i in range(len(S)):
    if S[i]=='C':
        c=1
    if c==1:
        if S[i]=='F':
            print('Yes')
            exit()
print('No')
