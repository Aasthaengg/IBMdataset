N, *a = map(int, open(0).read().split())

ans = 0
r = 0
x_xor = 0
x_sum = 0

for l in range(N):
    while (r == l) or (r < N and x_xor ^ a[r] == x_sum + a[r]):
        x_xor ^= a[r]
        x_sum += a[r]
        r += 1

    ans += r - l
    x_xor ^= a[l]
    x_sum -= a[l]
    
print(ans)
