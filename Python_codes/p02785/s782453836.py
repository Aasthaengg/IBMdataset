n,k = map(int,input().split())
h = list(map(int,input().split()))
if n <= k:
    print(0)
else:
    h.sort()
    ans = 0
    for i in range(n-k):
        ans += h[i]
    print(ans)