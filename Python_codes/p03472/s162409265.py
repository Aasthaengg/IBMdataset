import numpy as np
import math
N, H = map(int, input().split())
a_list = []
b_list = []
for _ in range(N):
    a, b = map(int, input().split())
    a_list.append(a)
    b_list.append(b)

a_max = max(a_list)
b_list.sort()
def judge(H, n, a_max, b_list):
    b_copy = b_list.copy()
    count = 0
    while H > 0:
        if len(b_copy) == 0:
            count += math.ceil(H / a_max)
            break
        else:
            b_max = b_copy.pop()
            if a_max > b_max:
                count += math.ceil(H / a_max)
                break
            else:
                H -= b_max
                count += 1
    if count <= n:
        return True
    return False

right = 10 ** 9
left = 1
while right != left:
    
    mid = (left + right) // 2
    if judge(H, mid, a_max, b_list):
        right = mid
    else:
        left = mid + 1

print(left)