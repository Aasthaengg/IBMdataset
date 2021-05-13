n = int(input())
a = list(map(int, input().split()))

ans = 0
xor = 0
sum = 0
r = 0

for l in range(n):
    while r < n and xor ^ a[r] == sum + a[r]:
        xor ^= a[r]
        sum += a[r]
        r += 1
    
    ans += r - l
    if l == r:
        r += 1
    else:
        sum -= a[l]
        xor ^= a[l]

print(ans)