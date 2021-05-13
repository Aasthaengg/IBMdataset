N, K = map(int, input().split())
V = list(map(int, input().split()))

ans = 0
for left in range(min(N, K) + 1):
    for right in range(min(N - left, K - left) + 1):
        tmp = V[:left] + V[N - right:]
        tmp.sort()
        score = 0
        count = K - left - right
        for i in tmp:
            if count <= 0:
                score += i
            else:
                if i < 0:
                    count -= 1
                else:
                    score += i
        # print (left, right, score, tmp)
        ans = max(ans, score)

print (ans)