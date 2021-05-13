import itertools
N,m,d = list(map(int,input().split(" ")))
f1 =(2* (N -d)) / (N ** 2)   # d = 1 N = N m = 2のケース
if d == 0:
    print(f1 * (m- 1) /2 )
else:
    print(f1 * (m- 1) )
