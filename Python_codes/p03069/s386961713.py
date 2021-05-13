import sys
import numpy as np
n = int(input())
s = list(map(str, input().rstrip()))

ss = s.count("#")
sd = s.count(".")

if ss == 0 or sd == 0:
    print(0)
    sys.exit()

s = np.array([x == "#" for x in s])

dp = np.zeros([2, n], dtype=int)

# dp0は黒の数、dp0は白の数
dp[0] = s
dp[1] = ~s

dp = dp.cumsum(axis=1)

# 白の数は「それ以降の」と読み替える
dp[1] = dp[1].max() - dp[1]

print(min((dp[0] + dp[1]).min(), ss, sd))