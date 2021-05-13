n, c = map(int, input().split(" "))

time = list()
for i in range(0, n):
    s, t, c = map(int, input().split(" "))
    time.append((s, t, c))

time_sorted = sorted(time, key=lambda x: (x[2], x[1]))

time_joined = list()
prev = None
for current in time_sorted:
    if prev is None:
        prev = current

    elif prev[2] == current[2] and prev[1] == current[0]:
        prev = (prev[0], current[1], current[2])

    else:
        time_joined.append(prev)
        prev = current

time_joined.append(prev)
# print(time_joined)

time_list = list()
for s, t, c in time_joined:
    time_list.append((s - 0.5, "s"))
    time_list.append((t, "t"))

time_list_sorted = sorted(time_list, key=lambda x: x[0])

current = 0
ans = 0

for t, s in time_list_sorted:
    if s == "s":
        current += 1
        ans = max(ans, current)
    else:
        current -= 1

print(ans)
