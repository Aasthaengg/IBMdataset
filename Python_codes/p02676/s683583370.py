K=int(input())
S=list(input())
a=[]
if len(S)<=K:
    print(''.join(S))
else:
    for i in range(0,K):
        a.append(S[i])
        
    print(''.join(a)+'...')
