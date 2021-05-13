N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

min_diff = 10**9
max_diff = -10**9
min_sum = 2 * 10**9
max_sum = 2

for x,y in XY:
    min_diff = min(x-y, min_diff)
    max_diff = max(x-y, max_diff)
    min_sum = min(x+y, min_sum)
    max_sum = max(x+y, max_sum)

print(max(max_sum-min_sum, max_diff-min_diff))