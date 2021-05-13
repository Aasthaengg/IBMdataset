times = [int(input()) for _ in range(5)]

rem = float("inf")
last = 0
for time in times:
    if time % 10 < rem and time % 10 != 0:
        rem = time % 10
        last = time
if last:
    times.remove(last)

total_time = 0
for time in times:
    if time % 10 == 0:
        total_time += time
    else:
        total_time += time + (10 - time % 10)
total_time += last

print(total_time)