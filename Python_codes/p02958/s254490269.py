import numpy as np
n = int(input())
a = list(map(int, input().split()))
if a == [i for i in range(1, n+1)] or sum(np.array(a)==np.array([i for i in range(1, n+1)]))==n-2:
    print("YES")
else:
    print("NO")