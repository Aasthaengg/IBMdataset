n = int(input())
a = list(map(int, input().split()))
if a[0] >= 1 or n == 0:
    print(1 if a[0] == 1 and n == 0 else -1)
    exit()
b = [0] * (n + 1)
for i in range(1, n + 1):
    b[i] = a[i] + b[i - 1]
v = 1
ans = 1
for i in range(n):
    v = min(b[n] - b[i], 2 * (v - a[i]))
    if v < a[i + 1]:
        print(-1)
        exit()
    ans += v
print(ans)