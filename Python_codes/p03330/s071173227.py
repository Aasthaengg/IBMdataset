n,c = map(int,input().split())

dll = []
for _ in range(c):
    dl = list(map(int,input().split()))
    dll.append(dl)

cll = []
for _ in range(n):
    cl = list(map(int,input().split()))
    cll.append(cl)


d_sum = [[0 for i in range(c)] for j in range(3)]

for i in range(c):
    for j in range(n):
        for k in range(n):
            d_sum[(j+k) % 3][i] += dll[cll[j][k]-1][i]

import itertools
c_set = [i for i in range(c)]
c_list = list(itertools.permutations(c_set, 3)) 

ans = float("inf")  
for c1, c2, c3 in c_list:
    tmp = d_sum[0][c1] + d_sum[1][c2] + d_sum[2][c3]
    if ans > tmp:
        ans = tmp

print(ans)