import numpy as np
n = int(input())
arr = np.array(list(map(int, input().split())))

big = arr.max()
arr = np.delete(arr, arr.argmax())

if big % 2 == 0:
    small = arr[(np.abs(arr - big // 2)).argmin()]
else:
    a = (np.abs(arr - (big + 1) // 2)).min()
    b = (np.abs(arr - (big) // 2)).min()
    if a <= b:
        small = arr[(np.abs(arr - (big + 1) // 2)).argmin()]
    else:
        small = arr[(np.abs(arr - big // 2)).argmin()]

print(big, small)