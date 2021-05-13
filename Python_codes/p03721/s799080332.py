N, K = map(int, input().split())			# "5 7" -> ["5", "7"] -> 5, 7 => N=5,K=7

from collections import defaultdict
d = defaultdict(lambda: 0)		#初期値を「-1」にする

for n in range(N):
  k, v = map(int, input().split())			# "5 7" -> ["5", "7"] -> 5, 7 => N=5,K=7
  d[k] += v

cnt=0
for k, v in sorted(d.items(), key=lambda x: x[0]):
  cnt += v
  if cnt >= K:
    print(k)
    exit(0)
