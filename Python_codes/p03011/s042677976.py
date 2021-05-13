ab_time, bc_time, ca_time = map(int, input().split())

time_sum_list = [ab_time, bc_time, ca_time]

max_time = max(ab_time, bc_time, ca_time)

min_time_line = sum(time_sum_list) - max_time
print(min_time_line)
