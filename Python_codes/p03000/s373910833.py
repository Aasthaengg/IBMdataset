from itertools import accumulate

N, X = [int(x) for x in input().split()]
L = list([int(x) for x in input().split()])

a = accumulate(L)

for key, i in enumerate(a):
    if i > X:
        print(key+1)
        exit()

print(N+1)
