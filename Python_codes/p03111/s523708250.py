N,A,B,C = map(int,input().split())
L = [int(input()) for i in range(N)]

from itertools import product

ans = 10**10
for pro in product([0,1,2,3], repeat= N):
    cost,lena,lenb,lenc = -30,0,0,0
    for i in range(N):
        if pro[i] == 1:
            lena += L[i]
            cost += 10
        elif pro[i] == 2:
            lenb += L[i]
            cost += 10
        elif pro[i] == 3:
            lenc += L[i]
            cost += 10
    if lena == 0 or lenb == 0 or lenc == 0:
        continue
    cost += abs(A-lena) + abs(B-lenb) + abs(C-lenc)
    ans = min(ans,cost)
print(ans)
