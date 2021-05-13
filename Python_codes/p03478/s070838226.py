N, A, B = [int(x) for x in input().split()]

ans = 0
for n in range(1, N + 1):
    m = n
    sum = 0
    while m > 0:
        sum += m % 10
        m //= 10
    if A <= sum <= B:
        ans += n

print(ans)