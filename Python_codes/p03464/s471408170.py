#B問題
import math
K = int(input())
A = list(map(int,input().split()))
B = A[::-1]

MIN = 0
MAX = 0
flag = 0
for i in range(K):
    if i == 0:
        if B[i] != 2:
            flag = 1
            break
        else:
            MIN = 2
            MAX = 3
    else:
        if MAX < B[i]:
            flag = 1
            break
        else:
            MAX = (MAX//B[i] + 1)*B[i]-1
            MIN = math.ceil(MIN/B[i])*B[i]
            if MAX < MIN:
                flag = 1
                break
if flag == 1:
    print(-1)
else:
    print(MIN,MAX)