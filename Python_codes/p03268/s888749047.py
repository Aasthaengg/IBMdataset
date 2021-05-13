n, k = list(map(int, input().split()))
s = n // k
ans = s ** 3

if k % 2 == 0:
    t = n // (k // 2) - s
    ans += t ** 3

print(ans)
