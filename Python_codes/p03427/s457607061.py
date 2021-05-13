S=str(int(input())+1)
N=[]
for s in S:
    N.append(int(s))
L=len(S)

if N==[9]*L:
    print(9*L)
else:
    print(N[0]-1+9*(L-1))
