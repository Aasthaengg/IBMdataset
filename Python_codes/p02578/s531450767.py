N = int(input())
A_list = list(map(int, input().split()))

height_list = [0] * N

for i in range(1, N):
    if height_list[i - 1] + A_list[i - 1] > A_list[i]:
        height_list[i] = height_list[i - 1] + A_list[i - 1] - A_list[i]

print(sum(height_list))