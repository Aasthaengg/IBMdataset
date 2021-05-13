import numpy as np

def list_element_add(l1, l2):
    result = np.array(l1) + np.array(l2)
    return result.tolist()

def solve(l, ave):
    for k in l:
        if k < ave:
            return False
    else:
        return True

n,m,x = map(int,input().split())
c = [list(map(int,input().split())) for _ in range(n)]
ans = 10**12

for i in range(2**n):
    understanding = [0]*m
    money = 0
    for j in range(n):
        if ((i >> j) & 1):
            money += c[j][0]
            understanding = list_element_add(understanding, c[j][1::])
    if solve(understanding, x):
        ans = min(ans,money)

print(ans if ans != 10**12 else '-1')