def min2(x,y):
    return x if x < y else y

from itertools import combinations
MOD = 2019
L, R = map(int, input().split())
data = [L%MOD]
for i in range(L+1, R+1):
    if data[0] ==i%MOD:
        break
    data.append(i%MOD)
res = float("inf")
for x, y in combinations(data, 2):
    res = min2((x*y)%MOD,res)
print(res)