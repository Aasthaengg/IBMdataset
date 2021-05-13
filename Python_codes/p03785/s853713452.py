N, C, K = map(int, input().split())
bus_count = 0
waiting_count = 0
time_limit = 0
D = [int(input()) for _ in range(N)]
D.sort()
# C == 1の場合にあロジックが崩壊してしまうわ
for i in range(N):
    T = D[i]
    waiting_count += 1
    if T > time_limit and not time_limit == 0:
        time_limit = T + K
        bus_count += 1
        waiting_count = 1
    if waiting_count == C:
        bus_count += 1
        waiting_count = 0
        time_limit = 0
    else:
        if waiting_count == 1:
            time_limit = T + K

if not waiting_count == 0:
    print(bus_count+1)
else:
    print(bus_count)
