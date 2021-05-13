n = int(input())

times = list(map(int, input().split(' ')))

summary = sum(times)

m = int(input())

for i in range(m):
    p, x = map(int, input().split(' '))
    print(summary - (times[p - 1] - x))