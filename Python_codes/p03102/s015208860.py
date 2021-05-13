n, m, c = [int(i) for i in input().split()]
bs = [int(i) for i in input().split()]
ans = 0
for _ in range(n):
    a_list = [int(i) for i in input().split()]
    cond = sum(a*b for a, b in zip(a_list, bs)) + c
    if cond > 0:
        ans += 1
print(ans)
