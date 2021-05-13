import math
N, K = map(int, input().split())
H = list(map(int, input().split()))
dp_list = [math.inf] * N
dp_list[0] = 0

for i, h in enumerate(H[:-1]):
  for j in range(1, min(K + 1, N - i)):
    cost_step = abs(H[i] - H[i + j])
    cost_total = dp_list[i] + cost_step
    if dp_list[i + j] > cost_total:
      dp_list[i + j] = cost_total
      
print(dp_list[-1])