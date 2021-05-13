N, A, B = map(int, input().split())
ans = 0
for i in range(1, N+1):
    j = i
    cnt = 0
    while j != 0:
        cnt += j % 10
        j //= 10
    if A <= cnt <= B: ans += i
print(ans)