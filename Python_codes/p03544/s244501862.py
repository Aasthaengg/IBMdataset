N = int(input())
prev, ans = 2, 1
for _ in range(N - 1):
    prev, ans = ans, ans + prev
print(ans)