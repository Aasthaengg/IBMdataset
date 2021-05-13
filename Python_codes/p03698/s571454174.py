S=list(input())
A=[]
for i in range(len(S)):
    for j in range(len(S)):
        if i<j and S[i]==S[j]:
            A.append('no')
            break
        else:
            A.append('yes')
if 'no' in A:
    print('no')
else:
    print('yes')