N = int(input())

limit2time = []

for i in range(N):
    time, limit = map(int, input().split())

    limit2time.append((limit, time))

limit2time  = sorted(limit2time, key=lambda x: x[0])

# print(limit2time)
cur = 0
for item in limit2time:
    # print(item)
    key, time = item
    if cur + time > key:
        print("No")
        break
    cur += time
else:
    print("Yes")