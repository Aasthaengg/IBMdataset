N, K = map(int, input().split())
H = list(map(int, input().split()))
if N <= K:
    print(0)
else:
    h_sorted = sorted(H,reverse=True)
    ans = sum(h_sorted[K:])
    print(ans)
