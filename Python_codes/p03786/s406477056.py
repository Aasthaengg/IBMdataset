import numpy as np
N = int(input())
A = np.array(list(map(int, input().split())))
A.sort()
cumsum = A.cumsum()
# sortした後にcumsumを２倍しても一つ隣のAより大きくなっていないものは最後に残れない
# 後ろから調べていって途切れたらそこから左みんなダメ
# print('A', A)
# print('cumsum', cumsum)

for i in range(N - 2, -1, -1):
    if A[i + 1] > cumsum[i] * 2:
        ans = N - 1 - i
        break
else:
    ans = N
print(ans)
