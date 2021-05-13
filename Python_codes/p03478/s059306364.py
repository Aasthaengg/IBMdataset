import numpy as np
                                                               
def ketawa(x):
    return sum(list(map(int, str(x))))
                                                               
N, A, B = map(int, input().split())
new_func = np.frompyfunc(ketawa, 1, 1)
arr = np.arange(1, N + 1)
result = new_func(arr)
print(np.sum(np.where((A <= result) & (result <= B), arr, 0)))