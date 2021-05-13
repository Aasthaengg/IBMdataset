S=input()
new_S1=list(reversed(S))
new_S2=''.join(new_S1)
if S==new_S2:
    A=S[0:len(S)//2]
    new_A1 = list(reversed(A))
    new_A2 = ''.join(new_A1)
    B=S[len(S)//2+1:len(S)]
    new_B1 = list(reversed(B))
    new_B2 = ''.join(new_B1)
    if A==new_A2 and B==new_B2:
        print('Yes')
    else:
        print('No')
else:
    print('No')

