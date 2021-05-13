
[A,B,C] = list(map(int,input().split()))
K = int(input())

ini = [A,B,C]
from itertools import permutations, combinations,combinations_with_replacement,product
a=['A','B','C']
Ls = list(combinations_with_replacement(a,K))

ans=0
for L in Ls:
    ini=[A,B,C]
    # print('ini:',ini)
    # print('L:',L)
    for i in L:
        # print('i:',i)
        if i=='A':
            ini[0]*=2
        elif i=='B':
            ini[1]*=2
        elif i=='C':
            ini[2]*=2
    ans=max(ans,sum(ini))
    # print('ans:',ans)

print(ans)
