n, k = map(int, input().split())
ans = 0
for i in range(1, n+1):
    sum = 1 / n
    jd = i
    while jd < k:
        sum *= 0.5
        jd *= 2
    ans += sum
print(ans)