n, q = map(int, raw_input().split(" "))
process = {}
schedule = []
sec = 0

for i in range(n):
    p, time = raw_input().split(" ")
    process[p] = int(time)
    schedule.append(p)

while len(schedule) != 0:
    p = schedule.pop(0)
    if process[p] - q > 0:
        process[p] -= q
        schedule.append(p)
        sec += q
    else:
        sec += process[p]
        print(p + " " + str(sec))