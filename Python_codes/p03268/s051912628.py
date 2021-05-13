n, k = map(int, input().split())

ans = 0
if k % 2 == 0:
    a = ((n+k//2)//k)
    ans += max(0, a*(a-1)*(a-2))
    ans += a*(a-1)*3
    ans += a

a = n//k
ans += max(0, a*(a-1)*(a-2))
ans += a*(a-1)*3
ans += a


print(ans)
