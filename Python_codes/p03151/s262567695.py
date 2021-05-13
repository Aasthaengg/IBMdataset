import numpy as np
import sys

N = int(input())
A = np.array(list(map(int, input().split())))
B = np.array(list(map(int, input().split())))

# print(A >= B)
# print(np.sort(A - B))
C = np.sort(A - B)
negative = C[C < 0]
positive = C[C >= 0]
positive = positive[::-1]
# print(negative, positive)
sum_neg = np.sum(negative)
cnt = 0
if len(negative) == 0:
    print(0)
    sys.exit()

for i in range(len(positive)):
    sum_neg += positive[i]
    cnt += 1
    if sum_neg >= 0:
        break

if sum_neg < 0:
    print(-1)
    sys.exit()
else:
    print(cnt + len(negative))
