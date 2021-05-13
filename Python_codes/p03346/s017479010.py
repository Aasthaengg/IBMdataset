n = int(input())
order = [0] * (n+1)
for i in range(n):
    p = int(input())
    order[p] = i+1
order[0] = 10**9

cnt = 0
ans = 0
for x, y in zip(order[:-1], order[1:]):
    if x > y:
        ans = max(cnt, ans)
        cnt = 0
    else:
        cnt += 1
ans = max(cnt, ans)

answer = n - ans - 1
print(answer)
