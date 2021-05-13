N, K = map(int, input().split())
V = list(map(int, input().split()))
lst = []
take = min(N, K)
ans = 0

for i in range(take+1):
    for j in range(take - i +1):
        lst = V[:i] + V[N - j:]
        lst.sort()
        cnt = 0
        for t in lst:
            if t < 0:
                cnt += 1
        d = min(cnt, K - ( i + j))
        del lst[:d]
        ans = max(ans, sum(lst))

print(ans)