n, k = map(int, input().split())

if n >= k:
    ans = (n-k+1)
else:
    ans = 0

for i in range(1, min(n+1, k)):
    cnt = 0
    score = i
    while score < k:
        score *= 2
        cnt += 1
    ans += pow(1/2, cnt)

ans /= n
print(ans)
