N = int(input())
x = list(input().split())
num = [int(x[i]) for i in range(N)]
num_sorted = sorted(num)
min_center = num_sorted[N // 2 - 1]
max_center = num_sorted[N // 2]

for i in range(N):
    if num[i] <= min_center:
        print(max_center)
    else:
        print(min_center)
