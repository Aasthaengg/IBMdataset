N = int(input())
cuisine = []
ans = 0
for _ in range(N):
    a, b = map(int, input().split())
    ans -= b
    cuisine.append(a+b)
cuisine = sorted(cuisine, reverse=True)
for i in range(N):
    if i % 2 == 1:
        continue
    ans += cuisine[i]
print(ans)
