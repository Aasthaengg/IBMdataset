
N = int(input())
ans = 0
for n in range(1, N+1):
    cnt = 0
    for i in range(1, n+1):
        if (n % i == 0) and (n % 2 == 1):
            cnt += 1
    if cnt == 8:
        ans += 1
print(ans)
