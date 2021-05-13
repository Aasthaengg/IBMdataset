import sys
import numpy as np
read = sys.stdin.read
readline = sys.stdin.readline

N, C = map(int, readline().split())
xv = np.array(read().split(), np.int64).reshape(N, 2)
v = xv[:, 1]
x = xv[:, 0]

ax = C - x[::-1]
cx = x.copy()
cx[1:] = cx[1:] - cx[:-1]
acx = C - x
acx[:-1] = acx[:-1] - acx[1:]

clockwise = v - cx
np.cumsum(clockwise, out=clockwise)
anticlockwise = v - acx
anticlockwise = np.cumsum(anticlockwise[::-1])

con_max = np.maximum.accumulate(clockwise)
anti_max = np.maximum.accumulate(anticlockwise)

answer = [0, con_max[-1], anti_max[-1]]

for i in range(N - 1):
    answer.append(clockwise[i] - x[i] + anti_max[N - i - 2])
    answer.append(anticlockwise[i] - ax[i] + con_max[N - i - 2])

print(max(answer))