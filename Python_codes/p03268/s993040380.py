N, K = map(int, input().split())

q = N//K
ans = q*q*q
if K % 2 == 1:
    print(ans)
else:
    p = (N+K//2)//K
    ans += p*p*p
    print(ans)
