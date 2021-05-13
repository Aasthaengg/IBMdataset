import numpy as np
D, N = map(int, input().split())

def cnt(n):
    tmp = 0
    n = n*1.0
    while n.is_integer():
        if (n/100.0).is_integer():
            tmp += 1
            n = n / 100.0
        else:
            break
            
    return tmp

coef = 100**D
whole = np.array([i*coef for i in range(1, 150)])
result = np.array(list(map(cnt, whole)))

print(whole[np.where(result==D)][N-1])