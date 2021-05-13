N = int(input())
h = list([int(x) for x in input().split()])

result = {0: 0}

for i in range(N-1):
    next_target = i + 1
    while next_target < N and next_target <= i + 2:
        cost = result[i] + abs((h[next_target] - h[i]))
        if not next_target in result:
            result[next_target] = cost
        else:
            if cost < result[next_target]:
                result[next_target] = cost
        next_target += 1

print(result[N-1])
