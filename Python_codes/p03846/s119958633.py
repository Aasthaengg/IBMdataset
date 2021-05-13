import numpy as np

N = int(input())
A = sorted(list(map(int, input().split())))

if len(A)%2 == 0:
    result = (2**(len(A)//2))%(10**9+7)
    a = np.arange(1, len(A), 2).tolist()
    a = sorted(a+a)
    if a == A:
        pass
    else:
        result = 0
else:
    result = 2**(len(A)//2)%(10**9+7)
    a = np.arange(2, len(A), 2).tolist()
    a = sorted([0]+a+a)
    if a == A:
        pass
    else:
        result = 0
print(result)