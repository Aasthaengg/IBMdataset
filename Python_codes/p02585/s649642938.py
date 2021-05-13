N, K = map(int, input().split())
P = [int(i) - 1 for i in input().split()]
Q = [int(i) for i in input().split()]
ans = - float('inf')
for i in range(N):
    now = i
    cnt = 0
    span = 0
    while True:
        span += 1
        cnt += Q[now]
        now = P[now]
        if now == i:
            break
    point = 0
    now = i
    for j in range(1, span + 1):
        point += Q[now]
        now = P[now]       
        if j > K:
            break
        value = point + (max(cnt, 0) * ((K - j) // span))
        ans = max(ans, value)
print(ans)