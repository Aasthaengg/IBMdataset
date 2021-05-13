n = int(input())
ts = list(map(int, input().split()))


normal_sum = sum(ts)

for _ in range(int(input())):
    no, time = map(int, input().split())
    print(normal_sum - ts[no-1] + time)
