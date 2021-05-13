import numpy as np

n = int(input())
a = np.array(list(map(int, input().split())))

# 負の数が奇数か偶数か
cnt = np.where(a < 0)[0].shape[0]
a = np.abs(a)

print(a.sum() if cnt % 2 == 0 else a.sum() - a.min() * 2)