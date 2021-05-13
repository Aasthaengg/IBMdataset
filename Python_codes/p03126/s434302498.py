N, M = map(int, input().split())
favorites = [list(map(int, input().split())) for _ in range(N)]

ans_dict = {}

for i in range(N):
    for j in range(1, favorites[i][0] + 1):
        food = favorites[i][j]
        if food in ans_dict:
            ans_dict[food] += 1
        else:
            ans_dict[food] = 1

count = 0
for k, v in ans_dict.items():
    if v == N:
        count += 1

print(count)
