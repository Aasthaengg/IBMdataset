n, k = map(int,input().split())
p = list(map(int,input().split()))
c = list(map(int,input().split()))

ans = -float('inf')
for i in range(n):
    score = []
    check = [0] * n
    now = i
    cycle = 0
    for _ in range(k):
        go = p[now] - 1
        if check[go] == 1:
            break
        now = go
        if len(score) == 0:
            score.append(c[now])
        else:
            score.append(score[-1] + c[now])
        check[now] = 1
        cycle += 1

    t = k // cycle
    m = k % cycle

    sum_cycle = score[-1]
    if m == 0:
        ans = max(sum_cycle * t, sum_cycle * (t - 1) + max(score), max(score), ans)
    else:
        ans = max(sum_cycle * t + max(score[:m]), sum_cycle * (t - 1) + max(score), max(score), ans)

print(ans)