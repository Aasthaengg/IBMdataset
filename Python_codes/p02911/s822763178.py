import numpy as np

N,K,Q = map(int, input().split())
n = [K-Q]*N
for _ in range(Q):
    n[int(input())-1] +=1

for an in n:
    if an > 0:
        print('Yes')
    else:
        print("No")