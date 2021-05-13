ab_time, bc_time, ca_time = map(int, input().split())

time_sum_list = [ab_time, bc_time, ca_time]

max_time_line = max(ab_time, bc_time, ca_time)

print(sum(time_sum_list) - max_time_line)