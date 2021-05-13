k, t = map(int, input().split())
A = sorted(map(int, input().split()))
if t == 1:
    print(k - 1)
else:
    dev = k - A[-1] + 1
    ans = max(0, (A[-1] // dev - 1) * dev + A[-1] % dev)
    print(ans)
