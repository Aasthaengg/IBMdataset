n, x = map(int,input().split())
origdat = list(map(int, input().split()))
from copy import deepcopy

res = 0

cnt = 0
dat = deepcopy(origdat)
for i in range(n):
    if dat[i] == 0:
        continue
    if dat[i] > x: # もし、xよりも大きな数なら、xにする
        res += dat[i] - x
        dat[i] = x
    if i == n-1:
        break
    if dat[i] + dat[i+1] > x:
        res += (dat[i] + dat[i+1]) - x
        dat[i+1] -= (dat[i] + dat[i+1]) - x
#print(dat)
print(res)