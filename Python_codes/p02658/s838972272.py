n = int(input())
a = list(map(int, input().split()))

ans = 1
threshold = 10 ** 18
if 0 in a:
    ans = 0
for i in range(n):
    ans *= a[i]
    if threshold < ans:
        ans = -1
        break

print(ans)