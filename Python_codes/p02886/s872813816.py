N = int(input())
d = list(map(int, input().split()))

ans = 0
for i in range(N):
    for j in range(N):
        x = d[i] * d[j]
        ans += x

dans = 0
for i in range(N):
    y = d[i] ** 2
    dans += y

fans = (ans - dans) // 2

print(fans)