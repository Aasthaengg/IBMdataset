import numpy as np

N,K,Q = map(int, input().split())
n = [0]*N
for _ in range(Q):
    n[int(input())-1] +=1

nn = np.array(n)
ans = K - Q + nn
for an in ans:
    if an > 0:
        print('Yes')
    else:
        print("No")