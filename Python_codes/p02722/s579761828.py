n = int(input())
ans = 1

for k in range(2, int(n ** 0.5) + 1):
    if n % k != 0:
        continue
    if (n // k) % k == 1:
        ans += 1
for i in range(2, 41):
    for k in range(2, n + 1):
        x = k ** i
        if x > n:
            break
        if n % x != 0:
            continue
        if (n // x) % k == 1:
            ans += 1
n -= 1
for k in range(1, int(n ** 0.5) + 1):
    if n % k != 0:
        continue
    if k * k == n or k == 1:
        ans += 1
    else:
        ans += 2
if(n == 1):
    ans -= 1
print(ans)