n, k, s = map(int,input().split())
ans = []
if s == 10**9:
    ans += [s]*k
    ans += [1]*(n-k)
    print(*ans)
    exit()

ans += [s]*k
ans += [10**9]*(n-k)
print(*ans)