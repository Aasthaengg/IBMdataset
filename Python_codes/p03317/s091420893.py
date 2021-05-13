n, k = map(int, input().split())
A = list(map(int, input().split()))

ans = (n-1) // (k-1)
if (n-1) % (k-1) > 0: ans += 1
print(ans)