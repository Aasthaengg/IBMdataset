import math
N = int(input())
step_list = list(map(int, input().split()))

dp_table = [math.inf] * N
dp_table[0] = 0

for i in range(1, N):
    if i <= 1:
        dp_table[i] = dp_table[i-1] + abs(step_list[i-1] - step_list[i])
    else:
        dp_table[i] = min(dp_table[i-1] + abs(step_list[i-1] - step_list[i]),
                          dp_table[i-2] + abs(step_list[i-2] - step_list[i]))

print(dp_table[N-1])
