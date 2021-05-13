def resolve():
    import math
    K = int(input())
    ans = []
    for i in range(1, K+1):
        for j in range(1, K+1):
            for p in range(1, K+1):
                q = math.gcd(i, j)
                ans.append(math.gcd(q, p))
    print(sum(ans))
resolve()