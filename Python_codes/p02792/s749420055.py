import numpy as np

N = int(input())
dp = np.zeros((10, 10)).astype(int)
dp[1, 1] = 1
ans = 1
for i in range(2, N + 1):

    i_str = str(i)
    i_start = int(i_str[0])
    i_end = int(i_str[-1])
    # print(i_start,i_end)
    if i_start == i_end:
        ans += 1
    ans += dp[i_end, i_start]*2
    dp[i_start, i_end] += 1
    # print(dp)
print(ans)
