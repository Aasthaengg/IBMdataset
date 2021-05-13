n, k = map(int, input().split())
ans = 0

if k % 2 == 1:
    p = n // k
    ans += pow(p, 3)
else:
    p = n//k
    q = (n + (k//2))//k
    ans += pow(p, 3) + pow(q, 3)

print(ans)