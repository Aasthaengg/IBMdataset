import numpy as np

n = int(input())
a = list(map(int,input().split()))
arr = np.array(a)

# 奇数がプラス、偶数がマイナス
cost1 = 0
cum = 0
for i in range(n):
    cum += arr[i]
    tmp = abs(cum) + 1
    if i%2==1 and cum<=0: cost1 += tmp ; cum += tmp
    if i%2==0 and cum>=0: cost1 += tmp ; cum -= tmp

# 奇数がマイナス、偶数がプラス
cost2 = 0
cum = 0
for i in range(n):
    cum += arr[i]
    tmp = abs(cum) + 1
    if i%2==1 and cum>=0: cost2 += tmp ; cum -= tmp
    if i%2==0 and cum<=0: cost2 += tmp ; cum += tmp


ans = min(cost1, cost2)
print(ans)

