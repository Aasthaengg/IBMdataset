n = int(input())
times = list(map(int, input().split()))
total = sum(times)
m = int(input())
for _ in range(m):
    index, newTime = map(int, input().split())
    print(total - times[index - 1] + newTime)
