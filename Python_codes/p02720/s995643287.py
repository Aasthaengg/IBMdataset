from itertools import chain

K = int(input())

L = 10
lunlun = [[] for _ in range(L+1)]

lunlun[1] = list(range(1,10))

for i in range(1,L):
    for x in lunlun[i]:
        r = x%10
        if r == 0:
            lunlun[i+1] += [x*10 + r, x*10 + r+1]
        elif r == 9:
            lunlun[i+1] += [x*10 + r-1, x*10 + r]
        else:
            lunlun[i+1] += [x*10 + r-1, x*10 + r, x*10 + r+1]

res = list(chain.from_iterable(lunlun))

print(res[K-1])