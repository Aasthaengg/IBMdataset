ans = 1<<100
for _ in range(int(input())):
    a, b = map(int, input().split())
    ans = min(ans, a+b)
print(ans)