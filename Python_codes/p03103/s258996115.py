N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

sorted_AB = sorted(AB, key=lambda x: x[0])

total_cost = 0
total_drink = 0
for i in range(N):
    total_cost += sorted_AB[i][0] * sorted_AB[i][1]
    total_drink += sorted_AB[i][1]

    if total_drink >= M:
        timing_count = i
        break

answer = total_cost - (total_drink - M) * sorted_AB[timing_count][0]

print(answer)