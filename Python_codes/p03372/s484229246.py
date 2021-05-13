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

clockwise = np.cumsum(v - cx)
anticlockwise = v - acx
anticlockwise = np.cumsum(anticlockwise[::-1])

con_max = np.maximum.accumulate(clockwise)
anti_max = np.maximum.accumulate(anticlockwise)

answer = [0, con_max[-1], anti_max[-1]]

clockwise = clockwise - x
anti_max = anti_max[::-1]
clockwise[:-1] = clockwise[:-1] + anti_max[1:]
anticlockwise = anticlockwise - ax
con_max = con_max[::-1]
anticlockwise[:-1] = anticlockwise[:-1] + con_max[1:]

answer.append(anticlockwise.max())
answer.append(clockwise.max())

print(max(answer))