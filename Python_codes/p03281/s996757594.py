N = int(input())

ans = 0
for n in range(3, N+1, 2):

    count = 1
    for i in range(3, n+1, 2):
        if n % i == 0:
            count += 1
        if n == 1:
            break
    if count == 8:
        ans += 1

print(ans)
