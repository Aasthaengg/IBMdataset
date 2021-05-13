n, m = map(int, input().split())
response_list = []
for _ in range(n):
    response = list(map(int, input().split()))
    response.pop(0)
    response_list.append(response)

cnt_list = [0]*m
for list in response_list:
    for i in list:
        cnt_list[i-1] += 1

ans = 0
for j in cnt_list:
    if j == n:
        ans += 1

print(ans)