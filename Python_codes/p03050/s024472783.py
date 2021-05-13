n = int(input())
ans = 0
p = 1
while True:
    if p ** 2 >= n:
        break
    if (n - p) % p == 0 and n % ((n - p) // p) != 0:
        ans += (n - p) // p
    p += 1

print(ans)