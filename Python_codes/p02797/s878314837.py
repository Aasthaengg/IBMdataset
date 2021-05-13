n, k, s = map(int, input().split())
ans = [s if i < k else (s + 1) % 10**9 for i in range(n)]
print(" ".join(map(str, ans)))
