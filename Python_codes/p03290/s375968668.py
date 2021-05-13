d, g = map(int, input().split())
pc = [list(map(int, input().split())) for i in range(d)]
ans = float("inf")

for i in range(2**d):
    sum_temp = 0
    count_temp = 0
    remain = set(range(1, d+1))
    for j in range(d):
        if i >> j & 1:
            sum_temp += 100 * (j + 1) * pc[j][0] + pc[j][1]
            count_temp += pc[j][0]
            remain -= {j+1}
    if sum_temp < g:
        use = max(remain)
        n = min(pc[use - 1][0], -(-(g - sum_temp) // (use * 100)))
        count_temp += n
        sum_temp += n * 100 * use
    if sum_temp >= g:
        ans = min(ans, count_temp)

print(ans)