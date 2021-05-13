n = int(input())
ans = pow(10, 10)

for i in range(n+1):
    cnt = 0
    j = n - i
    while i > 0:
        cnt += i % 6
        i //= 6

    while j > 0:
        cnt += j % 9
        j //= 9

    ans = min(ans, cnt)

print(ans)