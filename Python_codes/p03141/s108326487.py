n = int(input())

dish = []
ans = 0
for _ in range(n):
    a, b = map(int, input().split())
    dish.append(a + b)
    ans += -1 * b

dish.sort(reverse=True)
for i in range(n):
    if i % 2 == 0:
        ans += dish[i]
print(ans)