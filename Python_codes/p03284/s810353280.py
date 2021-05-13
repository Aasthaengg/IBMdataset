n, k = map(int, input().split())
ans = n % k
if ans > 1:
    ans = 1
print(ans)
