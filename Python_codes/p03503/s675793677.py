data = int(input())

F = [list(map(int, input().split())) for _ in range(data)]
P = [list(map(int, input().split())) for _ in range(data)]

max_score = -float('inf')
for pattern_i in range(1, 2**10):
  op_num = [0]*data
  for pos_i in range(10):
    if pattern_i & 1<<pos_i:
      for n_i in range(data):
        op_num[n_i] += F[n_i][pos_i]
  max_score = max(max_score, sum([p_i[op_num_i] for p_i, op_num_i in zip(P, op_num)]))

print(max_score)