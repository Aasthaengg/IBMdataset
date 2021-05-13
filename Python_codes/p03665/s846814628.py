import numpy as np
 
N, P = map(int, input().split())
A = list(map(int, input().split()))
odd = len([i for i in A if i%2!=0])
if odd==0 and P==0:
    ans = 2**N
elif odd==0 and P==1:
    ans = 0
else:
    ans = 2**(N-1)
print(ans)