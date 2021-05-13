import numpy as np
n, c = map(int, input().split())
channels = np.zeros((30, 10**5), dtype=np.int64)
for _ in range(n):
  s, t, c = map(int, input().split())
  s -= 1
  t -= 1
  c -= 1
  channels[c, s:t+1] += 1
newchannels = np.where(channels>1, 1, channels)
sums = newchannels.sum(axis=0)
print(sums.max())