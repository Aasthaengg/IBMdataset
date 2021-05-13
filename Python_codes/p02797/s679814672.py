n, k, s = [int(x) for x in input().split()]

if s == 10**9:
    print(*[s for _ in range(k)]+[1 for _ in range(n-k)], sep=" ")
else:
    print(*[s for _ in range(k)]+[s+1 for _ in range(n-k)], sep=" ")