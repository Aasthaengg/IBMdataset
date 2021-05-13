n = int(input())
a = list(map(int,input().split()))

from itertools import product

li = [-1,0,1]
cnt = 0
for v in product(li,repeat = n):
    L = []
    for i in range(n):
        L.append(v[i]+a[i])
    if any(x%2==0 for x in L):
        cnt +=1

print(cnt)