import math
import itertools
#n = int(input())
#n, d = list(input().split())
#n, l = list(map(int, input().split()))


n = int(input())
a = []
b = []

for i in range(n):
    x,y = [int(j) for j in input().split()]
    a.append(x)
    b.append(y)


mN = -1
posi = -1

for i in range(n):
    if a[i] > mN:
        mN = a[i]
        posi = i

print(mN+b[posi])

