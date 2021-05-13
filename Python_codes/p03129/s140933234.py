def resolve():
    import math
    N, K = map(int, input().split())
    print("YES" if math.ceil(N/2) >= K else "NO")
resolve()