n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]
ab.sort(key=lambda x: x[1])
total_time = 0

for i in range(n):
    total_time += ab[i][0]

    if total_time > ab[i][1]:
        print('No')
        exit()

print('Yes')
