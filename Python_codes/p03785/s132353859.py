n_people,bus_capacity,can_wait = map(int,input().split())
arriving_time_ls = [0] * n_people
for i in range(n_people):
    arriving_time_ls[i] = int(input())
arriving_time_ls.sort()

waiting_last = 0
bus_count = 0
for i in range(1,n_people):
    if (arriving_time_ls[i] - arriving_time_ls[waiting_last] > can_wait) or (i - waiting_last + 1 > bus_capacity):
        bus_count += 1
        waiting_last = i
bus_count += 1
print(bus_count)