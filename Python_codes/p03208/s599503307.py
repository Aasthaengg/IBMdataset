n, k = map(int, input().split())
h = [int(input()) for _ in range(n)]
h.sort()
print(min(hi - hj for hi, hj in zip(h[k-1:], h)))