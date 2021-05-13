n, m = map(int, input().split())
ans = 1

if abs(n - m) > 1:
    print(0)
    exit()

for i in range(1, n + 1):
    ans = ans*i%(10**9 + 7)

for i in range(1, m + 1):
    ans = ans*i%(10**9 + 7)

if (n + m)%2 == 0:
    ans = ans*2%(10**9 + 7)

print(ans)