num = list(map(int, input().split()))
min_range = num[0]
max_range = num[1]
n = num[2]
ans = len([i for i in range(min_range, max_range+1) if i % n <= 0])
print(ans)