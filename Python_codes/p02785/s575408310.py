N, K = map(int, input().split())
H = sorted(map(int, input().split()), reverse=True)
ans = sum(H[K:])
print(ans)