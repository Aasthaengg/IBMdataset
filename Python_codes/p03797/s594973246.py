N,M = map(int, input().split())
ans = 0
if 2 * N <= M:
    ans += N
    ans += int((M - (2 * N)) / 4)
else:
    ans += int(M / 2)

print(ans)