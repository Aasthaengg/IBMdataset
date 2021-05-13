N = int(input())
ans = [-1, -1]
for i in range(1, N + 1):
    cnt = 0
    tmp = i
    while tmp % 2 == 0:
        tmp //= 2
        cnt += 1
    if cnt > ans[0]:
        ans = [cnt, i]
print(ans[1])
