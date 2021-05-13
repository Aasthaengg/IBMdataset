import sys
# import numpy as np
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n, k = map(int, readline().split())
p = list(map(int, readline().split()))

tmp = [(i+1)/2 for i in p]
# cs = list(np.cumsum(tmp))

cs = [0]*n
cs[0] = tmp[0]
for i in range(len(tmp)-1):
    cs[i + 1] = cs[i] + tmp[i + 1]

if n == k:
    print(cs[-1])
    exit()
ans = 0
for i in range(n - k):
    ans = max(ans, cs[i + k] - cs[i])
print(ans)