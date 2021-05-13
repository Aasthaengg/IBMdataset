n, a, b = [int(s) for s in input().split()]
x_list = [int(s) for s in input().split()]
ans = 0
for i in range(n - 1):
    ans += min(a * (x_list[i + 1] - x_list[i]), b)
print(ans)