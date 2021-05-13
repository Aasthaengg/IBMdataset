current_time, remain_hour = map(int, input().split())

start_time = current_time + remain_hour

if start_time >= 24:
    start_next_day_time = start_time - 24
    print(start_next_day_time)
else:
    print(start_time)