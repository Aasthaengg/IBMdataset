n, k = map(int, input().split())
x = list(map(int, input().split()))
min_time  = abs(x[0]) + abs(x[-1] - x[0])

for i in range(n-k+1):
    time = min(abs(x[i]) + abs(x[i+k-1] - x[i]), \
        abs(x[i+k-1]) + abs(x[i+k-1] - x[i]))

    if time < min_time:
        min_time = time

print(min_time)