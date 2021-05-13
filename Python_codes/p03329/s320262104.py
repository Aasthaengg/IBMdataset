n = int(input())
min_time = [float('inf')] * (n+1)
min_time[0] = 0
for i in range(n):
    min_time[i+1] = min(min_time[i+1],min_time[i]+1)
    times_6 = 1
    while i+6**times_6<=n:
        min_time[i+6**times_6] = min(min_time[i+6**times_6],min_time[i]+1)
        times_6 += 1
    times_9 = 1
    while i+9**times_9<=n:
        min_time[i+9**times_9] = min(min_time[i+9**times_9],min_time[i]+1)
        times_9 += 1
print(min_time[-1])




