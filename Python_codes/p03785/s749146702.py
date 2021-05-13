N, C, K = [int(x) for x in input().split()]

times = [int(input()) for x in range(N)]
times.sort()

count = 0
minimum = None
passenger = 0

for t in times:
    passenger += 1
    if minimum  and (t - minimum) > K:
        count += 1
        minimum = t
        passenger = 1
    elif passenger == C:
        count += 1
        minimum = None
        passenger = 0
    elif minimum is None:
        minimum = t

if passenger:
    count += 1

print(count)
