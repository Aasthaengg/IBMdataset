n = int(input())
candy_map = []
candy_map.append(list(map(int, input().split())))
candy_map.append(list(map(int, input().split())))
ans = 0
for i in range(n):
    upper = sum(candy_map[0][:i])
    lower = sum(candy_map[1][i+1:])
    Sum = upper + lower + candy_map[0][i] + candy_map[1][i]
    ans = max(ans, Sum)
print(ans)

