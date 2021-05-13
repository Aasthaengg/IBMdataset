N, K = map(int, input().split())
Vs = list(map(int, input().split()))

ans = 0
for x in range(N+1):
    for y in range(N+1):
        if x+y > N or x+y > K:
            break
        rest = min(K-x-y, x+y)
        As = Vs[:x] + Vs[N-y:]
        As.sort()
        score = sum(As)
        for i in range(rest):
            if As[i] < 0:
                score -= As[i]
        ans = max(ans, score)

print(ans)
