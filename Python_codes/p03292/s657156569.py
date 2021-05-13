
A = list(map(int,input().split()))
#[A1,A2,A3] = list(map(int,input().split()))
# print(A)

from itertools import permutations
Ls = list(permutations(A))

ans=100000000
for L in Ls:
    # print('L:',L)
    cost=0
    for i in range(1,3):
        cost+=abs(L[i]-L[i-1])
        # print('i,c:', i,cost)
    # print('cost:', cost)
    ans = min(ans,cost)

print(ans)
