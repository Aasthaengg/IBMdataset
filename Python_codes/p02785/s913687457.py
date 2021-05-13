n, k = map(int, input().split())
H = list(map(int, input().split()))
H.sort()

if n <= k:
    print(0)
    exit()
ans = 0
for h in H[: n - k]:
    ans += h
print(ans)