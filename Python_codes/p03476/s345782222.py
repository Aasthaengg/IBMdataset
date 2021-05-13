
q = int(input())
lr = []
for i in range(q):
    lr.append([int(j)-1 for j in input().split()])

import math
def test_div(index):
    if index < 2:
        return 0
    elif index == 2:
        return 1
    max = math.ceil(math.sqrt(index))+1
    ls = []
    for i in range(2,max):
        if index % i == 0:
            return 0
    return 1

primes = [2]

import time
st = time.time()
#[0] * 100000
ls = []
for i in range(100000):
    ls.append(test_div(i+1))
ls_like = [0] * 100000
for i in range(100000):
    if ls[i]:
        if ls[(i+2)//2-1]:
            ls_like[i] = 1
        else:
            ls_like[i] = 0
    else:
        ls_like[i] = 0

ls_acc = [0]
for i in range(100000):
    ls_acc.append(ls_acc[-1] + ls_like[i])

#print(time.time()-st)


for i in range(q):
    [l,r] = lr[i]
    print(ls_acc[r+1]-ls_acc[l])
