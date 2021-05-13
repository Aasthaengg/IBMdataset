import math
step_n, max_jump = map(int, input().split())

step_list = list(map(int, input().split()))

dp_table = [math.inf] * (step_n)
dp_table[0] = 0

for i in range(1, step_n):
    min_from = max(0, i - max_jump)
    dp_table[i] = min(dp_table[j] + abs(step_list[i] - step_list[j]) for j in range(min_from, i))

print(dp_table[step_n-1])

