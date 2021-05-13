import itertools

S = list(input())
N = len(S)
# print('S:',S)

#onとoff
a = ['nashi','+']
Ls = list(itertools.product(a, repeat=N-1))
# print('Ls:',Ls)

out=0
dammy=[]
for L in Ls:
    # print('L,out:',L,out)
    dammy=[]
    for i in range(N):
        # print('dammy:',dammy)
        if i==N-1:
            dammy.append(S[i])
            out+=int(''.join(dammy))
            dammy=[]
        elif L[i] == 'nashi':
            dammy.append(S[i])
        else:
            dammy.append(S[i])
            out+=int(''.join(dammy))
            dammy=[]

print(out)
