n, k = list(map(int, input().split()))

if k != 1:
    ans = (n - (k - 1)) - 1
else:
    ans = 0
print(ans)