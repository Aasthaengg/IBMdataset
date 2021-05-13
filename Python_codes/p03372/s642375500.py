import sys
input = sys.stdin.readline

N, C = map(int, input().split())
sushi_array = [list(map(int, input().split())) for _ in range(N)]

# print(sushi_array)

left_max = 0
left_double_max = 0

left_array = [[0, 0] for _ in range(N+1)]

right_max = 0
right_double_max = 0

right_array = [[0, 0] for _ in range(N+1)]


left_sum = 0

for i, sushi in enumerate(sushi_array):
    left_sum += sushi[1]
    left_max = max(left_max, left_sum - sushi[0])
    left_double_max = max(left_double_max, left_sum - 2 * sushi[0])
    left_array[i+1][0] = left_max
    left_array[i+1][1] = left_double_max

right_sum = 0

for i, sushi in enumerate(sushi_array[::-1]):
    right_sum += sushi[1]
    right_max = max(right_max, right_sum - (C - sushi[0]))
    right_double_max = max(right_double_max, right_sum - 2 * (C - sushi[0]))
    right_array[N-i-1][0] = right_max
    right_array[N-i-1][1] = right_double_max

ans = 0

for left, right in zip(left_array, right_array):
    ans = max(ans, left[0]+right[1], left[1]+right[0])

print(ans)
