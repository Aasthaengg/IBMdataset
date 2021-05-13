times = [int(input()) for _ in range(5)]

total_time = 0
while times:
    if len(times) != 1:
        for i in range(len(times)):
            if times[i] % 10 == 0:
                total_time += times[i]
                times.remove(times[i])
                break
        else:
            rem = 0
            re_time = 0
            for time in times:
                if time % 10 > rem:
                    rem = time % 10
                    re_time = time
            total_time += re_time + (10 - rem)
            times.remove(re_time)
    else:
        total_time += times.pop()
        
print(total_time)