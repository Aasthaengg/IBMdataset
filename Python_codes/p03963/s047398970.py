n, k = map(int, input().split())

ans = k
ans *= pow(k - 1, n - 1)

print(ans)
