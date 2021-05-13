n, k = map(int, input().split())
ans = n - k
print(ans if ans >= 0 and k > 1 else 0)
