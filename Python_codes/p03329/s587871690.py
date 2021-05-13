def tmp_ans(total_cost, six_cost):
    res = 0
    tmp = n
    t = six_cost
    while t > 0:
        res += t % 6
        t //= 6
    t = total_cost - six_cost
    while t > 0:
        res += t % 9
        t //= 9
    return res

n = int(input())
ans = n
for x in range(n+1):
    ans = min(ans, tmp_ans(n, x))
print(ans)