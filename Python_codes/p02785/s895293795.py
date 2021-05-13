N, K = map(int, input().split())
H = list(map(int, input().split()))

sort_H = sorted(H, reverse=True)

ans = sum(sort_H[K:])

print(ans)

