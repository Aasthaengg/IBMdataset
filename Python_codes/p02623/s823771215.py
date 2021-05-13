n, m, k = map(int, input().split())

a = [0] + list(map(int, input().split()))
b = [0] + list(map(int, input().split()))

sum = 0
for i in b:
    sum += i

ans = 0
j = m
for i in range(0, n+1):
    sum += a[i]
    while j > 0 and sum > k:
        sum -= b[j]
        j -= 1
    if sum <= k:
        ans = max(ans, i+j)

print(ans)