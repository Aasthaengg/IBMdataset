import numpy as np
n = int(input())
n_list = np.array(list(map(int,input().split())))
syoujun_list =np.array(range(1,n+1))
different = n_list - syoujun_list
if np.count_nonzero(different) ==2 or np.count_nonzero(different) ==0:
    print('YES')
else:
    print('NO')