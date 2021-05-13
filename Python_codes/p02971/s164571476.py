from copy import deepcopy
n=int(input())
a=[int(input()) for _ in range(n)]
b = deepcopy(a)
b.sort()

for i in range(n):
    if a[i] == b[-1]:
        print(b[-2])
    else:
        print(b[-1])
