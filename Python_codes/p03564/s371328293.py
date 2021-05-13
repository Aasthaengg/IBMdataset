from itertools import product
N = int(input())
K = int(input())
cmin = 10**4
for x in product((0,1),repeat=N):
    cnt = 1
    for i in range(N):
        if x[i]==0:
            cnt = cnt*2
        else:
            cnt += K
    cmin = min(cmin,cnt)
print(cmin)