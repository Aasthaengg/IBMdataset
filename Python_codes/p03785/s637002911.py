N, C, K = map(int, input().split())
T = []
for i in range(N):
    T.append(int(input()))
    
T = sorted(T)

bus_time = False
human = 0
count = 0
for i in range(N):
    now = T[i]
    if bus_time == False:
        bus_time = now + K
        human = 1
        count += 1
    else:
        if now <= bus_time and human < C:
            human += 1
        else:
            bus_time = now + K
            human = 1
            count += 1

print(count)
