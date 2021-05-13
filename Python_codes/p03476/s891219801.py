# 累積和

import math
def is_prime(n):
    if n == 1: return False
    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False
    return True

# 2017数 かどうかのマップ
data = [0] * 10**5
# 処理系
for i in range(1, 10**5 + 1):
    if is_prime(i) and is_prime((i+1)//2):
        data[i-1] = 1

cumulative_sum = [0] * 10**5
cumulative_sum[0] = data[0]
for i in range(10**5 - 1):
    cumulative_sum[i+1] += cumulative_sum[i] + data[i+1]

# s_0 = 0 となるように
cumulative_sum = [0] + cumulative_sum

q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    print(cumulative_sum[r] - cumulative_sum[l-1])
    # print(sum(data[l:r+1]))
