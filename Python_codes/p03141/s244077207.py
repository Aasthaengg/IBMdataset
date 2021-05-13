n = int(input())
L = []
ans = 0
for _ in range(n):
    a, b = map(int, input().split())
    L.append([a, b, a + b])
L.sort(key=lambda x: x[2], reverse=True)
for i in range(0, n, 2):
    ans += L[i][0]
for i in range(1, n, 2):
    ans -= L[i][1]
print(ans)
