n = int(input())
ab = []
for _ in range(n):
    a, b = map(int, input().split())
    ab.append([a + b, a, b])
ab.sort(reverse = True)

num = (n + 1) // 2
ans = 0
for i in range(n):
    if i % 2 == 0:
        ans += ab[i][1]
    else:
        ans -= ab[i][2]
print(ans)