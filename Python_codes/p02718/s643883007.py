N, M =  map(int, input().split())
A = list(map(int, input().split()))
assert len(A) == N
# 商品iは得票Ai
# 総得票数の1/4M以上の商品をM個選ぶ
total = sum(A)
import math
thres = math.ceil(total / (4 * M))
count = len([i for i in range(N) if A[i] >= thres])
if count >= M:
  print('Yes')
else:
  print('No')