from collections import Counter
import numpy as np
N = int(input())
A = list(map(int, input().split()))
c = Counter(A)

# 2枚以上のところから-1, それ以外(2枚以上を優先しないなら1枚)のところから-1を繰り返す
# 3枚以上のところはそこから３枚とって２枚食べるということができるので偶数なら２、奇数なら１まで減らせる
values = np.array(sorted(list(c.values()), reverse=True))

values[(values % 2 != 0) & (values >= 3)] = 1
values[(values % 2 == 0) & (values >= 3)] = 2
values = values - 1
# print(values)
# print(values.sum())
if values.sum() % 2 == 0:
    print(len(values))
else:
    print(len(values) - 1)
