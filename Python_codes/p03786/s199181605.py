import numpy as np

N = int(input())
A = list(map(int, input().split()))
a = sorted(A)
res = list(np.cumsum(a))

ans = 0
idx = 1
for i in range(len(res)):
    num = res[i]
    if(idx <= i):
        idx = i+1
    while(num*2 >= a[idx]):
        num += a[idx]
        idx += 1
        
        if(idx >= len(res)-1):
            break
       
    if(idx >= len(res)-1):
        print(N-i)
        break