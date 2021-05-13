
n, k = map(int, input().split())

if k <= 1:
    ans = 0
else:
    nokori = n - k
    ans = nokori

print(ans)